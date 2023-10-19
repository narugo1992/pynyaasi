import pytest
import responses

from pynyaasi.nyaasi import NyaaSiClient
from test.testings import get_testfile


@pytest.fixture(autouse=True)
def _auto_load_fixture():
    try:
        responses._add_from_file(get_testfile('nyaasi.yaml'))
        yield
    finally:
        responses.reset()


@pytest.fixture()
def client():
    yield NyaaSiClient()
