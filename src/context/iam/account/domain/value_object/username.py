from context.shared.domain.types.varchar_type import VarcharType


class Username(VarcharType):
    _MIN_LENGTH = 1
    _MAX_LENGTH = 64

    def _min_length(self) -> int:
        return self._MIN_LENGTH

    def _max_length(self) -> int:
        return self._MIN_LENGTH

