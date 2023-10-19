import pytest

from pynyaasi.client import SizeProxy


@pytest.fixture
def size_0():
    return SizeProxy('0 Bytes')


@pytest.fixture()
def size_13_6_gib():
    return SizeProxy('13.6 GiB')


@pytest.mark.unittest
class TestClientSize:
    def test_size_proxy(self, size_13_6_gib, size_0):
        assert repr(size_13_6_gib) == '13.6 GiB'
        assert size_13_6_gib >= '10G'
        assert size_13_6_gib > '10G'
        assert size_13_6_gib <= '100G'
        assert size_13_6_gib < '100G'

        assert repr(size_0) == '0 Bytes'
        assert size_0 >= 0
        assert size_0 < '1 bytes'
