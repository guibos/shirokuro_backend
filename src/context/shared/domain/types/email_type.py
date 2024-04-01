from abc import ABC
from typing import Type

from context.shared.domain.types.validators.email_validator import EmailValidator
from context.shared.domain.types.validators.input_type_validator import InputTypeValidator


class EmailType(ABC, str, InputTypeValidator, EmailValidator):
    _INPUT_TYPE = str

    def __init__(self, value: str) -> None:
        self._validate(value)

    def _validate(self, value: str):
        self._validate_input_type(value)
        self._validate_email(value)

    def _allowed_input_type(self) -> Type:
        return self._INPUT_TYPE
