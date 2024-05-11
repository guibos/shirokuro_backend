from context.shared.domain.exception.security.security_base_error import SecurityBaseError


class UnauthorizedError(SecurityBaseError):
    _PRIVATE_MESSAGE_TEMPLATE = 'Unauthorized.'
    _PUBLIC_MESSAGE_TEMPLATE = 'Unauthorized.'

    def __init__(self):
        super().__init__(
            private_message=self._PRIVATE_MESSAGE_TEMPLATE,
            public_message=self._PUBLIC_MESSAGE_TEMPLATE,
            value=None,
            location=['Authorization']
        )