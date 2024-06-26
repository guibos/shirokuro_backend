from abc import ABC, abstractmethod

from context.shared.domain.bus.query.query import Query


class QueryHandler(ABC):

    @abstractmethod
    def __call__(self, query: Query):
        pass
