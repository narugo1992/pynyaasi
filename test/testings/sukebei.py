import logging
from itertools import islice

from responses import _recorder

from pynyaasi.client import Order, SortBy
from pynyaasi.sukebei import SukebeiClient, FilterType, CategoryType
from .testfile import get_testfile

logging.basicConfig(level=logging.DEBUG)


@_recorder.record(file_path=get_testfile('sukebei.yaml'))
def main():
    client = SukebeiClient()

    for _ in islice(client.iter_items('euphoria'), 200):
        pass

    for _ in islice(client.iter_items('euphoria', filter=FilterType.NO_REMAKES), 200):
        pass

    for _ in client.iter_items('euphoria', filter=FilterType.TRUSTED_ONLY):
        pass

    for _ in client.iter_items('euphoria', category=CategoryType.ART_ANIME):
        pass

    for _ in client.iter_items('euphoria', category=CategoryType.ART_ANIME, sort_by=SortBy.COMMENTS):
        pass

    for _ in client.iter_items('euphoria', category=CategoryType.ART_ANIME, sort_by=SortBy.COMMENTS, order=Order.ASC):
        pass

    _ = client.get_resource(3981804)
    _ = client.get_resource(3973877)


if __name__ == '__main__':
    main()
