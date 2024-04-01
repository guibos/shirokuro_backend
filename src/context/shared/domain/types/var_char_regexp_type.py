from abc import ABC
from typing import Type

from context.shared.domain.types.validators.input_type_validator import InputTypeValidator
from context.shared.domain.types.validators.regexp_validator import RegexpValidator


class VarCharRegexpType(str, InputTypeValidator, RegexpValidator, ABC):
    _ALLOWED_INPUT_TYPE = str

    def __init__(self, value: str) -> None:
        self._validate(value)

    def _validate(self, value: str):
        self._validate_input_type(value)
        self._validate_format(value)

    @property
    def _allowed_input_type(self) -> Type:
        return self._ALLOWED_INPUT_TYPE
