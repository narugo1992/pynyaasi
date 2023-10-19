import logging
from itertools import islice

from responses import _recorder

from pynyaasi.client import Order, SortBy
from pynyaasi.nyaasi import NyaaSiClient, FilterType, CategoryType
from .testfile import get_testfile

logging.basicConfig(level=logging.DEBUG)


@_recorder.record(file_path=get_testfile('nyaasi.yaml'))
def main():
    client = NyaaSiClient()

    for _ in islice(client.iter_items('fire force'), 200):
        pass

    for _ in islice(client.iter_items('fire force', filter=FilterType.NO_REMAKES), 200):
        pass

    for _ in client.iter_items('fire force', filter=FilterType.TRUSTED_ONLY):
        pass

    for _ in client.iter_items('fire force', category=CategoryType.ANIME_RAW):
        pass

    for _ in client.iter_items('fire force', category=CategoryType.ANIME_RAW, sort_by=SortBy.COMMENTS):
        pass

    for _ in client.iter_items('fire force', category=CategoryType.ANIME_RAW, sort_by=SortBy.COMMENTS, order=Order.ASC):
        pass

    _ = client.get_resource(1174590)
    _ = client.get_resource(1639366)
    _ = client.get_resource(1716268)


if __name__ == '__main__':
    main()
