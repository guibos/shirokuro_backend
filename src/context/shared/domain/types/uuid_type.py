import uuid
from typing import Optional


class UUIDType:
    def __init__(self, uuid_: Optional[str] = None) -> None:
        self._uuid = uuid.UUID(uuid_) if uuid_ else uuid.uuid4()

    def to_string(self) -> str:
        return str(self._uuid)
