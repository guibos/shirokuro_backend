from logging import Logger
from typing import Type, Dict

from context.shared.domain.bus.query.query import Query
from context.shared.domain.bus.query.query_bus import QueryBus
from context.shared.domain.bus.query.query_handler import QueryHandler
from context.shared.infrastructure.bus.query.exceptions.query_not_registered_error import QueryNotRegisteredError
from context.shared.infrastructure.bus.query.exceptions.query_registered_after_dispatch import \
    QueryRegisteredAfterDispatch


class QueryBusSync(QueryBus):
    _IS_SYNC = True

    def __init__(self, logger: Logger):
        self._mapping: Dict[Type[Query], QueryHandler] = {}
        self._ask_has_been_called = False
        self._logger = logger

    def register(self, query_class: Type[Query], handler: QueryHandler):
        self._guard_has_been_called()
        self._mapping[query_class] = handler

    def ask(self, query: Query):
        self._mark_as_asked()
        handler = self._get_handler(query)
        return handler(query)

    def is_sync(self):
        return self._IS_SYNC

    def _get_handler(self, query: Query):
        try:
            return self._mapping[type(query)]
        except KeyError as e:
            self._logger.critical(f'Query "%s" has not been registered.',
                                  type(query).__name__)
            raise QueryNotRegisteredError from e

    def _guard_has_been_called(self):
        if self._ask_has_been_called:
            raise QueryRegisteredAfterDispatch(
                'Trying to register a new handler after some query has been dispatched'
            )

    def _mark_as_asked(self):
        self._ask_has_been_called = True
