from abc import abstractmethod

from context.shared.domain.exception.invalid_length_error import InvalidLengthError
from context.shared.domain.exception.invalid_type_error import InvalidTypeError


class VarCharValidator:
    def _validate_length(self, value: str):
        if not self._min_length <= len(value) <= self._max_length:
            raise InvalidLengthError(value, self._min_length, self._max_length)

    @staticmethod
    def _validate_type(value: str):
        if not isinstance(value, str):
            raise InvalidTypeError(value, str)

    @property
    @abstractmethod
    def _min_length(self) -> int:
        pass

    @property
    @abstractmethod
    def _max_length(self) -> int:
        pass


