import random
import string
from abc import ABC

from context.shared.domain.types.var_char_type import VarCharType


class VarcharTypeMotherBase(VarCharType, ABC):
    def _get_random_string(self) -> str:
        length = random.randint(self._min_length, self._max_length)
        letters = string.printable
        return ''.join(random.choices(letters, k=length))
