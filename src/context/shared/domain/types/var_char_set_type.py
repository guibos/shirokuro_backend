from abc import ABC

from context.shared.domain.types.validators.char_set_validator import CharSetValidator
from context.shared.domain.types.validators.var_char_validator import VarCharValidator


class VarCharSetType(str, CharSetValidator, VarCharValidator, ABC):
    def __init__(self, value: str) -> None:
        self._validate(value)

    def _validate(self, value: str):
        self._validate_type(value)
        self._validate_length(value)
        self._validate_char_set(value)

