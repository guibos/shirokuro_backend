from typing import TypeVar, Generic

import rstr

from context.shared.domain.types.var_char_regexp_type import VarCharRegexpType

_T = TypeVar('_T', bound=VarCharRegexpType)


class VarCharRegexpTypeMotherBase(Generic[_T]):
    _MAX_TEST_CASES = 5

    def __init__(self, klass: type[_T]) -> None:
        self._klass = klass

    def random(self) -> _T:
        return self._klass(rstr.xeger(self._klass.regexp_pattern()))

    def test_cases(self):
        return [self.random() for _ in range(self._MAX_TEST_CASES)]
