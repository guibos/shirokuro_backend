from typing import re

from context.shared.domain.types.var_char_type import VarCharType


class Password(VarCharType):
    _REGEXP_PATTERN = re.compile('^.{0,64}$')

    @property
    def _regexp_pattern(self) -> re.Pattern:
        return self._REGEXP_PATTERN
