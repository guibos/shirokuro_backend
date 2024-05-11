import re
from typing import List, Union

from context.shared.domain.exception.bad_request.bad_request_error_base import BadRequestErrorBase


class InvalidPatternError(BadRequestErrorBase):
    _MESSAGE_TEMPLATE = 'Value provided does not match with pattern: "{}"'

    def __init__(self, value: str, pattern: re.Pattern, location: List[Union[str, int]]):
        message = self._MESSAGE_TEMPLATE.format(pattern.pattern)
        super().__init__(
            private_message=message,
            public_message=message,
            value=value,
            location=location
        )

