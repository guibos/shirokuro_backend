from typing import Iterable, List, Union

from context.shared.domain.exception.bad_request.bad_request_error_base import BadRequestErrorBase


class InvalidCharSetError(BadRequestErrorBase):
    _MESSAGE_TEMPLATE = 'Value provided contain forbidden characters: {}. Allowed characters are: {}.'

    def __init__(self,
                 value: str,
                 localization: List[Union[str, int]],
                 allowed_values: Iterable[str],
                 forbidden_values: Iterable[str]) -> None:
        allowed_text = '"' + '", "'.join(allowed_values) + '"'

        messages = [self._MESSAGE_TEMPLATE.format(value, forbidden_values,allowed_text)]

        super().__init__(
            value=value,
            localization=localization,
            public_messages=messages,
            private_messages=messages,
        )
