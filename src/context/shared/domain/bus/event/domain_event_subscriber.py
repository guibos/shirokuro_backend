from abc import ABC, abstractmethod
from typing import Any, Dict


class DomainEventSubscriber(ABC):

    @abstractmethod
    def subscribed_to(self) -> Dict[str, Any]:
        pass
