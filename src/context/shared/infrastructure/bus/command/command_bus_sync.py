from typing import Callable, Type

from context.shared.domain.bus.command.command import Command
from context.shared.domain.bus.command.command_bus import CommandBus
from context.shared.domain.bus.command.command_handler import CommandHandler
from context.shared.domain.bus.query.query import Query
from context.shared.domain.bus.query.query_bus import QueryBus
from context.shared.infrastructure.bus.handle_locator import HandleLocator


class CommandBusSync(CommandBus):
    def __init__(self):
        self._locator = HandleLocator()
        self._ask_has_been_called = False

    # TODO: typing
    def register(self, query_class: Type[Command], handler: CommandHandler):
        self._guard_has_been_called()
        self._locator.add(handler)

    def dispatch(self, command: Type[Command]):
        self._mark_as_asked()
        handler = self._locator.find(Command.__class__.__name__)
        return handler(command)

    def _guard_has_been_called(self):
        if self._ask_has_been_called:
            raise RuntimeError('Trying to register a new handler after some command has been dispatched')

    def _mark_as_asked(self):
        self._ask_has_been_called = True

