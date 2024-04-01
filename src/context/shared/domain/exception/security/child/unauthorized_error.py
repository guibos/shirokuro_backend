from context.shared.domain.exception.security.security_base_error import SecurityBaseError


class UnauthorizedError(SecurityBaseError):
    _PRIVATE_MESSAGE_TEMPLATE = 'Unauthorized.'
    _PUBLIC_MESSAGE_TEMPLATE = 'Unauthorized.'

    def __init__(self):
        super().__init__(
            private_messages=[self._PRIVATE_MESSAGE_TEMPLATE],
            public_messages=[self._PUBLIC_MESSAGE_TEMPLATE])