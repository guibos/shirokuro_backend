from typing import Type, Any, Union, List

from context.shared.domain.exception.bad_request.bad_request_error_base import BadRequestErrorBase


class InvalidTypeError(BadRequestErrorBase):
    _MESSAGE_TEMPLATE = 'Value type "{}" provided is not allowed. Allowed type is "{}"'

    def __init__(self, value: Any, location: List[Union[str, int]], valid_type: Type):
        message = self._MESSAGE_TEMPLATE.format(str(value),
                                                 type(value).__name__,
                                                 valid_type.__name__)
        super().__init__(
            private_message=message,
            public_message=message,
            value=value,
            location=location
        )
