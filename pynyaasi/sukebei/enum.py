from enum import Enum, unique

SUKEBEI_ENDPOINT = 'https://sukebei.nyaa.si'


@unique
class FilterType(str, Enum):
    NO_FILTER = '0'
    NO_REMAKES = '1'
    TRUSTED_ONLY = '2'


@unique
class CategoryType(str, Enum):
    ALL_CATEGORIES = '0_0'
    ART = '1_0'
    ART_ANIME = '1_1'
    ART_DOUJINSHI = '1_2'
    ART_GAMES = '1_3'
    ART_MANGA = '1_4'
    ART_PICTURES = '1_5'
    REAL_LIFE = '2_0'
    REAL_LIFE_PICTURES = '2_1'
    REAL_LIFE_VIDEOS = '2_2'
