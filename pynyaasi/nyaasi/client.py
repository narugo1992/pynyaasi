from typing import Optional

import requests

from .enum import NYAASI_ENDPOINT, FilterType, CategoryType
from ..client import BaseClient


class NyaaSiClient(BaseClient):
    __endpoint__ = NYAASI_ENDPOINT
    __filter_class__ = FilterType
    __default_filter__ = FilterType.NO_FILTER
    __category_class__ = CategoryType
    __default_category__ = CategoryType.ALL_CATEGORIES

    def __init__(self, session: Optional[requests.Session] = None):
        BaseClient.__init__(self, session)
