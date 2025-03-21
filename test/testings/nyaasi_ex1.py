import logging

import requests
from responses import _recorder

from .testfile import get_testfile

logging.basicConfig(level=logging.DEBUG)


@_recorder.record(file_path=get_testfile('nyaasi_ex1.yaml'))
def main():
    requests.get('https://nyaa.si/view/915257').raise_for_status()


if __name__ == '__main__':
    main()
