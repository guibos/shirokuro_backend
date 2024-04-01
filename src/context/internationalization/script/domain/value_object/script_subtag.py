import string
from typing import Set

from context.internationalization.shared.domain.abstract.subtag_field import SubtagField


class ScriptSubtag(SubtagField):
    _MIN_LENGTH = 4
    _MAX_LENGTH = 4
    _CHAR_SET = set(string.ascii_letters)

    @property
    def _char_set(self) -> Set[str]:
        return self._CHAR_SET

    @property
    def _min_length(self) -> int:
        return self._MIN_LENGTH

    @property
    def _max_length(self) -> int:
        return self._MAX_LENGTH
