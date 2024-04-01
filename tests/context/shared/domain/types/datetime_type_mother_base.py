import datetime
from typing import TypeVar, Generic, List

from context.shared.domain.types.datetime_type import DatetimeType

_T = TypeVar('_T', bound=DatetimeType)


class DatetimeTypeMotherBase(Generic[_T]):
    _MAX_TEST_CASES = 5

    def __init__(self, klass: type[_T]) -> None:
        self._klass = klass

    def random(self) -> _T:
        return self._klass.from_datetime(datetime.datetime.now())

    def test_cases(self) -> List[_T]:
        return [self.random() for _ in range(self._MAX_TEST_CASES)]
