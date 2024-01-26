from abc import ABC
from typing import List

from context.shared.domain.bus.event.domain_event import DomainEvent


class EventBus(ABC):
    def publish(self, events: List[DomainEvent]) -> None:
        pass
