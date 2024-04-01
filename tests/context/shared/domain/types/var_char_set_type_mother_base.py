import random
from typing import Generic, TypeVar

from context.shared.domain.types.var_char_set_type import VarCharSetType


_T = TypeVar('_T', bound=VarCharSetType)


class VarCharSetTypeMotherBase(Generic[_T]):

    def __init__(self, klass: type[_T]) -> None:
        self._klass = klass

    def random(self):
        length = random.randint(self._klass.MIN_LENGTH, self._klass.MAX_LENGTH)
        return ''.join(random.choices(list(self._klass.charset()), k=length))

    def random_min(self):
        return ''.join(random.choices(list(self._klass.charset()), k=self._klass.MIN_LENGTH))

    def random_max(self):
        return ''.join(random.choices(list(self._klass.charset()), k=self._klass.MAX_LENGTH))
