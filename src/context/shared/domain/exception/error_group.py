from typing import List, Tuple, override

from context.shared.domain.exception.error_base import ErrorBase
from context.shared.domain.exception.unit_error import UnitError


class ErrorGroup(ExceptionGroup):
    def __init__(self, message: str, exceptions: List[UnitError]):
        super().__init__(message, exceptions)

    @override
    def exceptions(self) -> List[UnitError]:
        return self.exceptions

TypeError
