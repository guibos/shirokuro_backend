from enum import Enum


class Scope(Enum):
    COLLECTION = 'collection'
    PRIVATE_USE = 'private-use'
    MACRO_LANGUAGE = 'macrolanguage'
    SPECIAL = 'special'
