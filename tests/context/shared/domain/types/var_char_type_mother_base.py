import random
import string
from abc import ABC
from typing import TypeVar, Generic

import rstr

from context.shared.domain.types.var_char_type import VarCharType


_T = TypeVar('_T', bound=VarCharType)


class VarCharTypeMotherBase(Generic[_T]):

    def __init__(self, klass: type[_T]) -> None:
        self._klass = klass

    def random_min(self):
        return rstr.xeger(f"^.{{{self._klass.min_length()}}}$")

    def random_max(self):
        return rstr.xeger(f"^.{{{self._klass.max_length()}}}$")

    def random(self):
        return rstr.xeger(f"^.{{{self._klass.min_length()},{self._klass.max_length()}}}$")

    def test_cases(self):
        cases = [self.random() for _ in range(10)]
        cases.append(self.random_min())
        cases.append(self.random_max())
        return cases
