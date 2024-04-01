from abc import abstractmethod, ABC
from typing import Any, Type

from context.shared.domain.exception.bad_request.child.invalid_type_error import InvalidTypeError


class InputTypeValidator(ABC):
    def _validate_input_type(self, input_type: Any):
        if not isinstance(input_type, self._allowed_input_type):
            raise InvalidTypeError(input_type, self._allowed_input_type)

    @property
    @abstractmethod
    def _allowed_input_type(self) -> Type:
        raise NotImplementedError
