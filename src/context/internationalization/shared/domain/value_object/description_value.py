from context.shared.domain.types.var_char_type import VarCharType


class DescriptionValue(VarCharType):
    """Every value of a :class:context.internationalization.shared.domain.value_object.description.Description"""
    _MIN_LENGTH = 1
    _MAX_LENGTH = 10

    @property
    def _min_length(self) -> int:
        return self._MIN_LENGTH

    @property
    def _max_length(self) -> int:
        return self._MAX_LENGTH

