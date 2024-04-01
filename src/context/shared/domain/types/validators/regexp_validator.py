import re
from abc import ABC, abstractmethod

from context.shared.domain.exception.bad_request.child.invalid_pattern_error import InvalidPatternError


class RegexpValidator(ABC):
    def _validate_format(self, value: str):
        if not self.regexp_pattern().match(value):
            raise InvalidPatternError(value, self.regexp_pattern())

    @classmethod
    @abstractmethod
    def regexp_pattern(cls) -> re.Pattern:
        pass
