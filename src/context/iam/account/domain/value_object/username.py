from context.shared.domain.types.var_char_type import VarCharType


class Username(VarCharType):
    _MIN_LENGTH = 1
    _MAX_LENGTH = 64

    def _min_length(self) -> int:
        return self._MIN_LENGTH

    def _max_length(self) -> int:
        return self._MIN_LENGTH

