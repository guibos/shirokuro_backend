import re


class InvalidPatternError(TypeError):
    _MESSAGE_TEMPLATE = '"{}" value is does not match with pattern: "{}"'

    def __init__(self, value: str, pattern: re.Pattern):
        super().__init__(self._MESSAGE_TEMPLATE.format(str(value), pattern.pattern))
