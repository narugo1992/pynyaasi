import re
import warnings
from contextlib import contextmanager
from dataclasses import dataclass
from enum import Enum, unique
from typing import Optional, Type, Any, Iterator
from urllib.parse import urljoin

import requests
from hbutils.scale import size_to_bytes
from hbutils.system import urlsplit
from pyquery import PyQuery as pq

from ..utils import load_text_from_enum, get_session, unix_timestamp_to_datetime, load_from_enum


@unique
class SortBy(str, Enum):
    COMMENTS = 'comments'
    SIZE = 'size'
    DATE = 'id'
    SEEDERS = 'seeders'
    LEECHERS = 'leechers'
    DOWNLOADS = 'downloads'


@unique
class Order(str, Enum):
    DESC = 'desc'
    ASC = 'asc'


@contextmanager
def _suppress_warning():
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore')
        yield


@dataclass
class SizeProxy:
    raw: str

    def __repr__(self):
        return self.raw

    @property
    def _bytes(self):
        if 'bytes' in self.raw.lower():
            return int(' '.join(re.split(r'\s+', self.raw)[:-1]))
        else:
            return size_to_bytes(self.raw)

    def __gt__(self, other):
        with _suppress_warning():
            return self._bytes > size_to_bytes(other)

    def __ge__(self, other):
        with _suppress_warning():
            return self._bytes >= size_to_bytes(other)

    def __lt__(self, other):
        with _suppress_warning():
            return self._bytes < size_to_bytes(other)

    def __le__(self, other):
        with _suppress_warning():
            return self._bytes <= size_to_bytes(other)


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
    is_red: bool

    @property
    def datetime(self):
        return unix_timestamp_to_datetime(self.timestamp)

    @property
    def time(self) -> str:
        return self.datetime.isoformat()

    @property
    def size(self) -> SizeProxy:
        return SizeProxy(self.size_raw)


class BaseClient:
    __endpoint__: Optional[str] = None
    __filter_class__: Optional[Type[Enum]] = None
    __default_filter__ = None
    __category_class__: Optional[Type[Enum]] = None
    __default_category__ = None

    def __init__(self, session: Optional[requests.Session] = None):
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
            is_red = bool(row.has_class('danger'))
            category_raw = urlsplit(row('td:nth-child(1) a').attr('href')).query_dict['c']
            category = load_from_enum(category_raw, self.__category_class__)

            comment_boxes = list(row('td:nth-child(2) a#comments').items())
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
                is_trusted, is_red
            )

    # noinspection PyShadowingBuiltins
    def iter_items(self, query: str = '', filter=..., category=..., sort_by=None, order=Order.DESC,
                   from_page: int = 1):
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
