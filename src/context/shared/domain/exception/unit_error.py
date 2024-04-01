from typing import List

from context.shared.domain.exception.error_base import ErrorBase


class UnitError(ExceptionGroup):
    def __init__(self, message: str, exceptions: List[ErrorBase]):
        super().__init__(message, exceptions)

