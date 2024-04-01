from abc import ABC
from uuid import UUID


class IdType(UUID, ABC):
    pass
