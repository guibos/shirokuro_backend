from typing import List, Tuple, override

from context.shared.domain.exception.error_base import ErrorBase


class ErrorGroup(ExceptionGroup):
    def __init__(self, message: str, exceptions: List[ErrorBase]):
        super().__init__(message, exceptions)

