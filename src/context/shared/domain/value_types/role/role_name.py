import string
from typing import Set

from context.shared.domain.types.var_char_set_type import VarCharSetType


class RoleName(VarCharSetType):
    _CHARSET = set(string.ascii_letters + string.digits + ':_')
    _MIN_LENGTH = 5
    _MAX_LENGTH = 32

    @property
    def _char_set(self) -> Set[str]:
        return self._CHARSET

    @property
    def _min_length(self) -> int:
        return self._MIN_LENGTH

    @property
    def _max_length(self) -> int:
        return self._MAX_LENGTH
