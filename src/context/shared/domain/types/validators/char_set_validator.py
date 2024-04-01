from abc import abstractmethod
from typing import Set

from context.shared.domain.exception.invalid_char_set_error import InvalidCharSetError


class CharSetValidator:
    def _validate_char_set(self, value: str):
        forbidden_chars = set(value).difference(self._char_set)
        if forbidden_chars:
            raise InvalidCharSetError(value, forbidden_chars, self._char_set)

    @property
    @abstractmethod
    def _char_set(self) -> Set[str]:
        pass
