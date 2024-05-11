from context.shared.domain.exception.internal.internal_base_error import InternalBaseError


class UnexpectedError(InternalBaseError):
    _MESSAGE_TEMPLATE = 'Unexpected error.'
    def __init__(self, traceback: str) -> None:
        super().__init__(
            private_message=traceback,
            public_message=self._MESSAGE_TEMPLATE,
            value=None,
            location=[],
        )
