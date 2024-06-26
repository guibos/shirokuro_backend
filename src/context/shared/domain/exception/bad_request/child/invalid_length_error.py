from typing import List, Union

from context.shared.domain.exception.bad_request.bad_request_error_base import BadRequestErrorBase


class InvalidLengthError(BadRequestErrorBase):
    _MESSAGE_TEMPLATE = 'Value provided length must be between {} and {}'

    def __init__(self, value: str, location: List[Union[str, int]], min_length: int, max_length) -> None:
        message = self._MESSAGE_TEMPLATE.format(min_length, max_length)

        super().__init__(
            value=value,
            location=location,
            public_message=message,
            private_message=message
        )
