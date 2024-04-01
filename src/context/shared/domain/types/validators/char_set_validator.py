from abc import abstractmethod, ABC
from typing import Set

from context.shared.domain.exception.bad_request.child.invalid_char_set_error import InvalidCharSetError


class CharSetValidator(ABC):
    @classmethod
    @abstractmethod
    def charset(cls) -> Set[str]:
        raise NotImplementedError

    def _validate_char_set(self, value: str):
        forbidden_chars = set(value).difference(self.charset())
        if forbidden_chars:
            raise InvalidCharSetError(value, forbidden_chars, self.charset())
