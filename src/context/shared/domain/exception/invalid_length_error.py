class InvalidLengthError(TypeError):
    _MESSAGE_TEMPLATE = 'Value length "{}" must be between {} and {}'

    def __init__(self, value: str, min_length: int, max_length) -> None:
        super().__init__(self._MESSAGE_TEMPLATE.format(value, min_length, max_length))
