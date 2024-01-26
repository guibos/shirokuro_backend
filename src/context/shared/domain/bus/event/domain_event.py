import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from tkinter import EventType
from typing import Optional, Any, Dict
from uuid import UUID


class DomainEvent(ABC):
    def __init__(self, aggregate_id: str, event_id: Optional[str], occurred_on: Optional[str] = None) -> None:
        self._aggregate_id = aggregate_id
        self._event_id = event_id if event_id else uuid.uuid4().hex
        self._occurred_on = occurred_on if occurred_on else datetime.now()

    @classmethod
    @abstractmethod
    def from_primitive(cls, aggregate_id: str, body: Dict[str, Any], event_id: str, occurred_on: Optional[str]) -> 'DomainEvent':
        pass

    @abstractmethod
    def event_name(self) -> str:
        pass

    def to_primitives(self) -> Dict[str, Any]:
        pass

    def aggregate_id(self) -> str:
        return self._aggregate_id

    def event_id(self) -> str:
        return self._event_id

    def occurred_on(self) -> datetime:
        return self._occurred_on
