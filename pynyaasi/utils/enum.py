import re
from enum import Enum
from typing import Type


def _strip_name(text):
    """
    Strip special characters and convert to lowercase.

    :param text: The input text
    :type text: str
    :return: The stripped and lowercase version of the input text
    :rtype: str
    """
    return re.sub(r'[\W_]+', '', text).lower()


def load_from_enum(text, enum_class: Type[Enum]):
    """
    Load an Enum member from a given text.

    :param text: The text to match with Enum values
    :type text: str
    :param enum_class: The Enum class to search in
    :type enum_class: Type[Enum]
    :return: The Enum member corresponding to the text
    :rtype: Enum
    :raises ValueError: If the text does not match any Enum values
    :raises TypeError: If the input value is not a string
    """
    if isinstance(text, str):
        for key, item in enum_class.__members__.items():
            if item.value == text or _strip_name(item.name) == _strip_name(text):
                return item

        raise ValueError(f'Unknown value of {text!r} from {enum_class!r}.')
    else:
        raise TypeError(f'Unknown enum value - {text!r}.')


def load_text_from_enum(text, enum_class: Type[Enum]):
    """
    Load text from an Enum member or a text value.

    :param text: The text or Enum member
    :type text: Union[str, Enum]
    :param enum_class: The Enum class to search in
    :type enum_class: Type[Enum]
    :return: The text value corresponding to the input
    :rtype: Any
    :raises TypeError: If the input value is not a string or Enum member
    """
    if hasattr(text, 'value'):
        return text.value
    elif isinstance(text, str):
        return load_from_enum(text, enum_class).value
    else:
        raise TypeError(f'Unknown enum value - {text!r}.')
