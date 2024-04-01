from typing import Type


class InvalidTypeError(TypeError):
    _MESSAGE_TEMPLATE = '"{}" value is not allowed type: "{}". Allowed type is "{}"'

    def __init__(self, value, valid_type: Type):
        super().__init__(self._MESSAGE_TEMPLATE.format(str(value), type(value).__name__, valid_type.__name__))
