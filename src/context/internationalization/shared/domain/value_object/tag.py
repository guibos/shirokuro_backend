from context.shared.domain.types.var_char_type import VarCharType


class Tag(VarCharType):
    _MIN_LENGTH = 1
    _MAX_LENGTH = 20
    @property
    def _min_length(self) -> int:
        return self._MIN_LENGTH

    @property
    def _max_length(self) -> int:
        return self._MAX_LENGTH