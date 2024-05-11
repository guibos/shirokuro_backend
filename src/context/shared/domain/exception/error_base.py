from typing import List, Any, Union, Optional


class ErrorBase(Exception):
    def __init__(self, private_message: str, public_message: str, value: Optional[Any], location: List[Union[str, int]]):
        super().__init__(private_message)
        self._private_message = private_message
        self._public_message = public_message
        self._value = value
        self._location = location

    @property
    def private_message(self) -> str:
        return self._private_message

    @property
    def public_message(self) -> str:
        return self._public_message

    @property
    def value(self) -> Any:
        return self._value

    @property
    def location(self) -> List[str]:
        return self._location
