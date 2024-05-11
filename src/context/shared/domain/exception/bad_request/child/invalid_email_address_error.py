from typing import List, Union

from context.shared.domain.exception.bad_request.bad_request_error_base import BadRequestErrorBase


class InvalidEmailAddressError(BadRequestErrorBase):
    def __init__(self, value: str, location: List[Union[str, int]], invalid_email_address_reasons: str):
        super().__init__(
            value=value,
            location=location,
            public_message=invalid_email_address_reasons,
            private_message=invalid_email_address_reasons,

        )
