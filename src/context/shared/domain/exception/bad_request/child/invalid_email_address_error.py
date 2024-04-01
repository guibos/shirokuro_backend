from typing import List, Union

from context.shared.domain.exception.bad_request.bad_request_error_base import BadRequestErrorBase


class InvalidEmailAddressError(BadRequestErrorBase):
    def __init__(self, value: str, localization: List[Union[str, int]], invalid_email_address_reasons: List[str]):
        super().__init__(
            value=value,
            localization=localization,
            public_messages=invalid_email_address_reasons,
            private_messages=invalid_email_address_reasons,

        )
