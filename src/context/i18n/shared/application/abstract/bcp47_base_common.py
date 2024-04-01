import dataclasses
from abc import ABC
from datetime import datetime
from uuid import UUID


@dataclasses.dataclass(frozen=True, kw_only=True)
class BCP47BaseCommon(ABC):
    """Mixin that must be used by all BCP47 types. Only contains fields that are common between all BCP47 types."""
    id: UUID
    description: str
    created_at: datetime
    updated_at: datetime
