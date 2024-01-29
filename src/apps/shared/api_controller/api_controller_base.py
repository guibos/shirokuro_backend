from abc import ABC, abstractmethod

from context.shared.domain.bus.command.command import Command
from context.shared.domain.bus.command.command_bus import CommandBus
from context.shared.domain.bus.query.query import Query
from context.shared.domain.bus.query.query_bus import QueryBus
from context.shared.domain.bus.query.response import Response


class ApiControllerBase(ABC):
    def __init__(self, query_bus: QueryBus, command_bus: CommandBus):
        self._query_bus = query_bus
        self._command_bus = command_bus

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass

    def _ask(self, query: Query) -> Response:
        return self._query_bus.ask(query)

    def _dispatch(self, command: Command) -> None:
        self._command_bus.dispatch(command)

    def _command_is_sync(self) -> bool:
        return self._command_bus.is_sync()
