import re
import warnings
from contextlib import contextmanager
from dataclasses import dataclass

from hbutils.scale import size_to_bytes


@contextmanager
def _suppress_warning():
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore')
        yield


def _text_to_bytes(text):
    if 'bytes' in text.lower():
        return int(' '.join(re.split(r'\s+', text)[:-1]))
    else:
        with _suppress_warning():
            return size_to_bytes(text)


@dataclass
class SizeProxy:
    raw: str

    def __repr__(self):
        return self.raw

    @property
    def _bytes(self):
        return _text_to_bytes(self.raw)

    def __gt__(self, other):
        with _suppress_warning():
            return self._bytes > _text_to_bytes(other)

    def __ge__(self, other):
        with _suppress_warning():
            return self._bytes >= _text_to_bytes(other)

    def __lt__(self, other):
        with _suppress_warning():
            return self._bytes < _text_to_bytes(other)

    def __le__(self, other):
        with _suppress_warning():
            return self._bytes <= _text_to_bytes(other)
