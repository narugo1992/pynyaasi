import pytest

from pynyaasi.nyaasi import CategoryType
from pynyaasi.utils import load_from_enum, load_text_from_enum


@pytest.mark.unittest
class TestUtilsEnum:
    def test_load_from_enum(self):
        assert load_from_enum('1_4', CategoryType) == CategoryType.ANIME_RAW
        assert load_from_enum('0_0', CategoryType) == CategoryType.ALL_CATEGORIES

        with pytest.raises(ValueError):
            _ = load_from_enum('xxx', CategoryType)
        with pytest.raises(TypeError):
            _ = load_from_enum(123, CategoryType)

    def test_load_text_from_enum(self):
        assert load_text_from_enum(CategoryType.ALL_CATEGORIES, CategoryType) == CategoryType.ALL_CATEGORIES
        assert load_text_from_enum(CategoryType.ANIME_RAW, CategoryType) == CategoryType.ANIME_RAW

        assert load_text_from_enum('0_0', CategoryType) == CategoryType.ALL_CATEGORIES
        assert load_text_from_enum('1_4', CategoryType) == CategoryType.ANIME_RAW

        with pytest.raises(TypeError):
            _ = load_text_from_enum(1, CategoryType)
