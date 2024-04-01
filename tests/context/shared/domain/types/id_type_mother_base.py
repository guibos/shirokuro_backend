import uuid
from typing import TypeVar, Generic

from context.shared.domain.types.id import IdType

_T = TypeVar('_T', bound=IdType)


class IdTypeMotherBase(Generic[_T]):
    _MAX_TEST_CASES = 5

    def __init__(self, klass: type[_T]) -> None:
        self._klass = klass

    def random(self):
        return self._klass(uuid.uuid4())

    def test_cases(self):
        return [self.random() for _ in range(self._MAX_TEST_CASES)]
