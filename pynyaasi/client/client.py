import re
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Type, Any, Iterator
from urllib.parse import urljoin

import requests
from hbutils.system import urlsplit
from pyquery import PyQuery as pq

from .directory import DirectoryTreeNode, Directory, File
from .enum import SortBy, Order
from .size import SizeProxy
from ..utils import load_text_from_enum, get_session, unix_timestamp_to_datetime, load_from_enum


@dataclass
class ListItem:
    id: int
    category: Any
    comments: int
    title: str
    url: str
    torrent_download_url: str
    magnet_url: str
    size_raw: str
    timestamp: int
    seeders: int
    leechers: int
    downloads: int
    is_trusted: bool
    is_remake: bool
    is_batch: bool

    @property
    def datetime(self):
        """
        Get the datetime of the item's timestamp.

        :return: The datetime of the item.
        :rtype: datetime.datetime
        """
        return unix_timestamp_to_datetime(self.timestamp)

    @property
    def time(self) -> str:
        """
        Get the timestamp of the item in ISO format.

        :return: The timestamp of the item in ISO format.
        :rtype: str
        """
        return self.datetime.isoformat()

    @property
    def size(self) -> SizeProxy:
        """
        Get the size of the item as a SizeProxy object.

        :return: The size of the item.
        :rtype: SizeProxy
        """
        return SizeProxy(self.size_raw)


@dataclass
class ResourceItem:
    id: int
    category: Any
    title: str
    information: str
    torrent_download_url: str
    magnet_url: str
    size_raw: str
    timestamp: int
    seeders: int
    leechers: int
    downloads: int
    is_trusted: bool
    is_remake: bool
    is_batch: bool
    info_hash: str
    submitter: str
    submitter_url: Optional[str]
    description_md: str
    directory_tree: DirectoryTreeNode

    @property
    def datetime(self):
        """
        Get the datetime of the item's timestamp.

        :return: The datetime of the item.
        :rtype: datetime.datetime
        """
        return unix_timestamp_to_datetime(self.timestamp)

    @property
    def time(self) -> str:
        """
        Get the timestamp of the item in ISO format.

        :return: The timestamp of the item in ISO format.
        :rtype: str
        """
        return self.datetime.isoformat()

    @property
    def size(self) -> SizeProxy:
        """
        Get the size of the item as a SizeProxy object.

        :return: The size of the item.
        :rtype: SizeProxy
        """
        return SizeProxy(self.size_raw)


class BaseClient:
    """
    A base class for clients that interact with websites like nyaa.si.

    Attributes:
        - __endpoint__: The base URL for the website.
        - __filter_class__: The class that defines filtering options.
        - __default_filter__: The default filtering option.
        - __category_class__: The class that defines item categories.
        - __default_category__: The default item category.

    Methods:
        - iter_items_by_page: Iterates through items on the website by page.
        - iter_items: Iterates through items on the website with paging support.
        - get_resource: Retrieves detailed information about a resource.
    """

    __endpoint__: Optional[str] = None
    __filter_class__: Optional[Type[Enum]] = None
    __default_filter__ = None
    __category_class__: Optional[Type[Enum]] = None
    __default_category__ = None

    def __init__(self, session: Optional[requests.Session] = None):
        """
        Initialize the BaseClient.

        :param session: An optional requests.Session object.
        :type self: Optional[requests.Session]
        """
        assert self.__endpoint__ is not None, f'__endpoint__ of {self.__class__.__name__} class not assigned.'
        assert self.__filter_class__ is not None, \
            f'__filter_class__ of {self.__class__.__name__} class not assigned.'
        assert self.__default_filter__ is not None, \
            f'__default_filter__ of {self.__class__.__name__} class not assigned.'
        assert self.__category_class__ is not None, \
            f'__category_class__ of {self.__class__.__name__} class not assigned.'
        assert self.__default_category__ is not None, \
            f'__default_category__ of {self.__class__.__name__} class not assigned.'

        self._session = session or get_session()

    # noinspection PyShadowingBuiltins
    def iter_items_by_page(self, query: str = '', filter=..., category=..., sort_by=None, order=Order.DESC,
                           page: int = 1) -> Iterator[ListItem]:
        """
        Iterates through items on the website by page.

        :param query: The search query.
        :type query: str
        :param filter: The filter for items.
        :param category: The category for items.
        :param sort_by: The sorting option.
        :param order: The sorting order (ascending or descending).
        :type order: Order
        :param page: The page number to start from.
        :type page: 1
        :return: An iterator of ListItem objects.
        :rtype: Iterator[ListItem]
        """
        params = {
            'f': load_text_from_enum(filter if filter is not ... else self.__default_filter__,
                                     self.__filter_class__),
            'c': load_text_from_enum(category if category is not ... else self.__default_category__,
                                     self.__category_class__),
            'q': query,
        }
        if sort_by is not None:
            params['s'] = load_text_from_enum(sort_by, SortBy)
            params['o'] = load_text_from_enum(order, Order)
        params['p'] = str(page)

        resp = self._session.get(self.__endpoint__, params=params)

        resp.raise_for_status()
        page = pq(resp.text)

        main_table = page('table.torrent-list')
        for row in main_table('tbody tr').items():
            is_trusted = bool(row.has_class('success'))
            is_remake = bool(row.has_class('danger'))
            is_batch = bool(row.has_class('warning'))
            category_raw = urlsplit(row('td:nth-child(1) a').attr('href')).query_dict['c']
            category = load_from_enum(category_raw, self.__category_class__)

            comment_boxes = list(row('td:nth-child(2) a.comments').items())
            if comment_boxes:
                comments = int(comment_boxes[0].text())
            else:
                comments = 0

            ta = row('td:nth-child(2) a:nth-last-child(1)')
            title = ta.attr('title')
            url = urljoin(resp.request.url, ta.attr('href'))
            id_ = int(urlsplit(url).path_segments[-1])

            torrent_download_url = urljoin(resp.request.url,
                                           row('td:nth-child(3) i.fa-download').parent('a').attr('href'))
            magnet_url = row('td:nth-child(3) i.fa-magnet').parent('a').attr('href')

            size_raw = row('td:nth-child(4)').text().strip()
            timestamp = int(row('td:nth-child(5)').attr('data-timestamp'))
            seeders = int(row('td:nth-child(6)').text())
            leechers = int(row('td:nth-child(7)').text())
            downloads = int(row('td:nth-child(8)').text())

            yield ListItem(
                id_, category, comments, title, url,
                torrent_download_url, magnet_url,
                size_raw, timestamp, seeders, leechers, downloads,
                is_trusted, is_remake, is_batch,
            )

    # noinspection PyShadowingBuiltins
    def iter_items(self, query: str = '', filter=..., category=..., sort_by=None, order=Order.DESC,
                   from_page: int = 1):
        """
        Iterates through items on the website with paging support.

        :param query: The search query.
        :type query: str
        :param filter: The filter for items.
        :param category: The category for items.
        :param sort_by: The sorting option.
        :param order: The sorting order (ascending or descending).
        :type order: Order
        :param from_page: The page number to start from.
        :type from_page: 1
        :return: An iterator of ListItem objects.
        :rtype: Iterator[ListItem]
        """
        page = from_page
        while True:
            iterator = self.iter_items_by_page(query, filter, category, sort_by, order, page)

            try:
                first_item = next(iterator)
            except StopIteration:
                break

            yield first_item
            yield from iterator

            page += 1

    def get_resource(self, id_: int):
        """
        Retrieves detailed information about a resource.

        :param id_: The ID of the resource.
        :type id_: int
        :return: A ResourceItem object with resource details.
        :rtype: ResourceItem
        """
        resp = self._session.get(f'{self.__endpoint__}/view/{id_}')
        resp.raise_for_status()
        page = pq(resp.text)

        panels = list(page('body > .container > .panel').items())

        # basic information
        first_block = panels[0]
        is_trusted = first_block.has_class('panel-success')
        is_remake = first_block.has_class('panel-danger')
        is_batch = first_block.has_class('panel-warning')
        title = first_block('.panel-heading .panel-title').text()
        torrent_download_url = urljoin(resp.request.url, first_block('.panel-footer a:nth-child(1)').attr('href'))
        magnet_url = first_block('.panel-footer a:nth-child(2)').attr('href')

        # header arguments
        arguments = {}
        for row in first_block('.panel-body .row').items():
            labels = list(row('.col-md-1').items())
            contents = list(row('.col-md-5').items())
            assert len(labels) == len(contents), f'Labels ({len(labels)}) and contents {len(contents)} not match.'

            for label, content in zip(labels, contents):
                label_text = re.sub(r'[\W_]+', '_', label.text().lower()).strip('_')
                content_text = content.text().strip()
                if label_text == 'category':
                    category_raw = urlsplit(urljoin(resp.request.url,
                                                    content('a:nth-last-child(1)').attr('href'))).query_dict['c']
                    arguments[label_text] = load_from_enum(category_raw, self.__category_class__)
                elif label_text == 'date':
                    arguments['timestamp'] = int(content.attr('data-timestamp'))
                elif label_text == 'submitter':
                    if list(content('a').items()):
                        arguments['submitter'] = content('a').text().strip()
                        arguments['submitter_url'] = urljoin(resp.request.url, content('a').attr('href'))
                    else:
                        arguments['submitter'] = content.text().strip()
                        arguments['submitter_url'] = None
                elif label_text in {'seeders', 'leechers'}:
                    arguments[label_text] = int(content.text().strip())
                elif label_text == 'completed':
                    arguments['downloads'] = int(content.text().strip())
                elif label_text == 'file_size':
                    arguments['size_raw'] = content_text.strip()
                else:
                    arguments[label_text] = content_text.strip()

        # description
        description_md = page('#torrent-description').html()

        # folder tree
        third_block = panels[2]
        list_header = third_block('.panel-body > ul > li')

        def _recursive_extraction(element):
            if list(element.children('a.folder')):
                _folder_name = element.children('a.folder').text().strip()
                items = element.children('ul').children('li')
                return Directory(_folder_name, [_recursive_extraction(item) for item in items.items()])

            elif list(element.children('i.fa-file')):
                _file_raw_size = element('.file-size').text().strip().strip('(').strip(')').strip()
                element.remove('.file-size')
                _file_name = element.text().strip()
                return File(_file_name, _file_raw_size)

            else:
                assert False, f'Unknown element in folder extraction - {element!r}.'  # pragma: no cover

        file_node = _recursive_extraction(list_header)

        return ResourceItem(
            id=id_, title=title,
            torrent_download_url=torrent_download_url,
            magnet_url=magnet_url,
            is_trusted=is_trusted,
            is_batch=is_batch,
            is_remake=is_remake,
            description_md=description_md,
            directory_tree=file_node,
            **arguments
        )
