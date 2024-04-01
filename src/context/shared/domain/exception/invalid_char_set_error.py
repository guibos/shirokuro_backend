from typing import List, Iterable


class InvalidCharSetError(TypeError):
    _MESSAGE_TEMPLATE = 'Value "{}" contain forbidden characters: {}. Allowed characters are: {}.'

    def __init__(self, value: str, allowed_values: Iterable[str], forbidden_values: Iterable[str]) -> None:
        forbidden_text = '"' + '", "'.join(allowed_values) + '"'
        allowed_text = '"' + '", "'.join(allowed_values) + '"'
        super().__init__(self._MESSAGE_TEMPLATE.format(value, forbidden_values, allowed_text))
