import random
import string
from abc import ABC

from context.shared.domain.types.varchar_type import VarcharType


class VarcharTypeMotherBase(VarcharType, ABC):
    def _get_random_string(self) -> str:
        length = random.randint(self._min_length, self._max_length)
        letters = string.printable
        return ''.join(random.choices(letters, k=length))
