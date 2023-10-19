from typing import Optional

import requests

from .enum import NYAASI_ENDPOINT, FilterType, CategoryType
from ..client import BaseClient


class NyaaSiClient(BaseClient):
    """
    A client class for accessing the nyaa.si website.

    The `NyaaSiClient` class is a subclass of `BaseClient` and provides specific functionality for accessing the nyaa.si website.

    :param session: An optional `requests.Session` object to be used for making HTTP requests.
    :type session: Optional[requests.Session]

    :ivar __endpoint__: The base endpoint URL for the nyaa.si website.
    :vartype __endpoint__: str
    :ivar __filter_class__: The available filter options for search queries on nyaa.si.
    :vartype __filter_class__: FilterType
    :ivar __default_filter__: The default filter option for search queries on nyaa.si.
    :vartype __default_filter__: FilterType
    :ivar __category_class__: The available category options for search queries on nyaa.si.
    :vartype __category_class__: CategoryType
    :ivar __default_category__: The default category option for search queries on nyaa.si.
    :vartype __default_category__: CategoryType
    """

    __endpoint__ = NYAASI_ENDPOINT
    __filter_class__ = FilterType
    __default_filter__ = FilterType.NO_FILTER
    __category_class__ = CategoryType
    __default_category__ = CategoryType.ALL_CATEGORIES

    def __init__(self, session: Optional[requests.Session] = None):
        """
        Initialize a new NyaaSiClient instance.

        :param session: An optional `requests.Session` object to be used for making HTTP requests.
        :type session: Optional[requests.Session]
        """
        BaseClient.__init__(self, session)
