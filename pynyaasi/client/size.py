import re
import warnings
from contextlib import contextmanager
from dataclasses import dataclass

from hbutils.scale import size_to_bytes


@contextmanager
def _suppress_warning():
    """
    A context manager that suppresses warnings temporarily.

    This context manager captures and temporarily suppresses warnings that occur within the context. It can be used to avoid displaying warning messages in specific parts of the code.

    Usage:
    ```python
    with _suppress_warning():
        # Code where warnings are temporarily suppressed
    ```

    :raises: Any exceptions or warnings that occur within the context are not displayed.
    """
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore')
        yield


def _text_to_bytes(text):
    """
    Convert a text representation of size to bytes.

    This function takes a text representation of a size (e.g., "1.5 GB") and converts it to the equivalent number of bytes.

    :param str text: The text representation of the size.
    :return: The size in bytes.
    :rtype: int

    :raises: It may raise warnings related to size conversions, which are temporarily suppressed during the conversion.
    """
    if isinstance(text, str) and 'bytes' in text.lower():
        return int(' '.join(re.split(r'\s+', text)[:-1]))
    else:
        with _suppress_warning():
            return size_to_bytes(text)


@dataclass
class SizeProxy:
    """
    Represents a proxy for managing and comparing sizes.

    The `SizeProxy` data class is designed to handle and compare sizes represented as text.

    :param str raw: The raw text representation of the size.

    :ivar raw: The raw text representation of the size.
    :vartype raw: str
    """

    raw: str

    def __repr__(self):
        return self.raw

    @property
    def _bytes(self):
        """
        Get the size in bytes.

        :return: The size in bytes.
        :rtype: int
        """
        return _text_to_bytes(self.raw)

    def __gt__(self, other):
        """
        Compare if the size is greater than another size.

        :param other: The size to compare with.
        :type other: str
        :return: True if the size is greater than the other size, False otherwise.
        :rtype: bool
        """
        with _suppress_warning():
            return self._bytes > _text_to_bytes(other)

    def __ge__(self, other):
        """
        Compare if the size is greater than or equal to another size.

        :param other: The size to compare with.
        :type other: str
        :return: True if the size is greater than or equal to the other size, False otherwise.
        :rtype: bool
        """
        with _suppress_warning():
            return self._bytes >= _text_to_bytes(other)

    def __lt__(self, other):
        """
        Compare if the size is less than another size.

        :param other: The size to compare with.
        :type other: str
        :return: True if the size is less than the other size, False otherwise.
        :rtype: bool
        """
        with _suppress_warning():
            return self._bytes < _text_to_bytes(other)

    def __le__(self, other):
        """
        Compare if the size is less than or equal to another size.

        :param other: The size to compare with.
        :type other: str
        :return: True if the size is less than or equal to the other size, False otherwise.
        :rtype: bool
        """
        with _suppress_warning():
            return self._bytes <= _text_to_bytes(other)
