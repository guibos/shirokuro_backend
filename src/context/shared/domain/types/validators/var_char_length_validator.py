from abc import ABC, abstractmethod

from context.shared.domain.exception.bad_request.child.invalid_length_error import InvalidLengthError


class VarCharLengthValidator(ABC):

    def _validate_length(self, value: str):
        if not self.min_length() <= len(value) <= self.max_length():
            raise InvalidLengthError(value, self.min_length(), self.max_length())

    @classmethod
    @abstractmethod
    def min_length(cls):
        pass

    @classmethod
    @abstractmethod
    def max_length(cls):
        pass
