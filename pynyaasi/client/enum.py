from enum import unique, Enum


@unique
class SortBy(str, Enum):
    """
    Enumeration representing sorting options for search results.

    The `SortBy` enumeration defines different attributes by which search results can be sorted, such as comments, size, date, seeders, leechers, and downloads.

    Each option in the enumeration corresponds to a specific sorting attribute for search results.

    :cvar COMMENTS: Sort by the number of comments.
    :cvar SIZE: Sort by file size.
    :cvar DATE: Sort by date.
    :cvar SEEDERS: Sort by the number of seeders.
    :cvar LEECHERS: Sort by the number of leechers.
    :cvar DOWNLOADS: Sort by the number of downloads.
    """
    COMMENTS = 'comments'
    SIZE = 'size'
    DATE = 'id'
    SEEDERS = 'seeders'
    LEECHERS = 'leechers'
    DOWNLOADS = 'downloads'


@unique
class Order(str, Enum):
    """
    Enumeration representing the order in which search results should be sorted.

    The `Order` enumeration defines two options for sorting order: descending (DESC) and ascending (ASC). This enumeration is typically used in combination with `SortBy` to specify the sorting order of search results.

    :cvar DESC: Sort in descending order.
    :cvar ASC: Sort in ascending order.
    """
    DESC = 'desc'
    ASC = 'asc'
