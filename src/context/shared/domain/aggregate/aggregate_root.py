from abc import ABC
from typing import List

from context.shared.domain.bus.event.domain_event import DomainEvent


class AggregateRoot(ABC):

    def __init__(self):
        self._domain_events = []

    def pull_domain_events(self) -> List[DomainEvent]:
        domain_events = self._domain_events
        self._domain_events = []
        return domain_events

    def _record(self, domain_event: DomainEvent) -> None:
        self._domain_events.append(domain_event)
