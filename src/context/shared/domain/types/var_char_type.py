from abc import ABC
from typing import Type

from context.shared.domain.types.validators.input_type_validator import InputTypeValidator
from context.shared.domain.types.validators.var_char_length_validator import VarCharLengthValidator


class VarCharType(str, InputTypeValidator, VarCharLengthValidator, ABC):
    _ALLOWED_INPUT_TYPE = str

    def __init__(self, value: str) -> None:
        self._validate(value)

    def _validate(self, value: str):
        self._validate_input_type(value)
        self._validate_length(value)

    def _allowed_input_type(self) -> Type:
        return self._ALLOWED_INPUT_TYPE
