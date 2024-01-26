from abc import ABC, abstractmethod

from context.shared.domain.bus.query.query import Query
from context.shared.domain.bus.query.response import Response


class QueryBus(ABC):

    @abstractmethod
    def ask(self, query: Query) -> Response:
        pass
