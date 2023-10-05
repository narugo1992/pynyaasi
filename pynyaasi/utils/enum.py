import re
from enum import Enum
from typing import Type


def _strip_name(text):
    return re.sub(r'[\W_]+', '', text).lower()


def load_from_enum(text, enum_class: Type[Enum]):
    if isinstance(text, str):
        for key, item in enum_class.__members__.items():
            if item.value == text or _strip_name(item.name) == _strip_name(text):
                return item

        raise ValueError(f'Unknown value of {text!r} from {enum_class!r}.')
    else:
        raise TypeError(f'Unknown enum value - {text!r}.')


def load_text_from_enum(text, enum_class: Type[Enum]):
    if hasattr(text, 'value'):
        return text.value
    elif isinstance(text, str):
        return load_from_enum(text, enum_class).value
    else:
        raise TypeError(f'Unknown enum value - {text!r}.')
