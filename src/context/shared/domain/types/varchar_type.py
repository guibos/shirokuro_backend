from abc import abstractmethod, ABC


class VarcharType(str, ABC):
    @property
    @abstractmethod
    def _min_length(self) -> int:
        pass

    @property
    @abstractmethod
    def _max_length(self) -> int:
        pass

    def to_string(self) -> str:
        return str(self)
