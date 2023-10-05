from enum import Enum, unique

NYAASI_ENDPOINT = 'https://nyaa.si'


@unique
class FilterType(str, Enum):
    NO_FILTER = '0'
    NO_REMAKES = '1'
    TRUSTED_ONLY = '2'


@unique
class CategoryType(str, Enum):
    ALL_CATEGORIES = '0_0'
    ANIME = '1_0'
    ANIME_AMV = '1_1'
    ANIME_ENGLISH = '1_2'
    ANIME_NON_ENGLISH = '1_3'
    ANIME_RAW = '1_4'
    AUDIO = '2_0'
    AUDIO_LOSSLESS = '2_1'
    AUDIO_LOSSY = '2_2'
    LITERATURE = '3_0'
    LITERATURE_ENGLISH = '3_1'
    LITERATURE_NON_ENGLISH = '3_2'
    LITERATURE_RAW = '3_3'
    LIVE_ACTION = '4_0'
    LIVE_ACTION_ENGLISH = '4_1'
    LIVE_ACTION_IDOL_PV = '4_2'
    LIVE_ACTION_NON_ENGLISH = '4_3'
    LIVE_ACTION_RAW = '4_4'
    PICTURES = '5_0'
    PICTURES_GRAPHICS = '5_1'
    PICTURES_PHOTOS = '5_2'
    SOFTWARE = '6_0'
    SOFTWARE_APPS = '6_1'
    SOFTWARE_GAMES = '6_2'
