from enum import unique, Enum


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
