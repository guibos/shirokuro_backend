from typing import List, Any, Union


class ErrorBase(Exception):
    def __init__(self, private_messages: List[str], public_messages: List[str], localization: List[Union[str, int]], value: Any):
        super().__init__(' '.join(private_messages))
        self._private_messages = private_messages
        self._public_messages = public_messages
        self._localization = localization
        self._value = value

    @property
    def localization(self):
        return self._localization

    @property
    def value(self):
        return self._value

    @property
    def private_message(self) -> List[str]:
        return self._private_messages

    @property
    def public_message(self) -> List[str]:
        return self._public_messages
