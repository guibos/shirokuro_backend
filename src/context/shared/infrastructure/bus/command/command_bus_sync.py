from logging import Logger
from typing import Type, Dict

from context.shared.domain.bus.command.command import Command
from context.shared.domain.bus.command.command_bus import CommandBus
from context.shared.domain.bus.command.command_handler import CommandHandler
from context.shared.infrastructure.bus.command.exceptions.command_not_registered_error import CommandNotRegisteredError
from context.shared.infrastructure.bus.command.exceptions.command_registered_after_dispatch import \
    CommandRegisteredAfterDispatch


class CommandBusSync(CommandBus):
    _IS_SYNC = True

    def __init__(self, logger: Logger):
        self._mapping: Dict[Type[Command], CommandHandler] = {}
        self._ask_has_been_called = False
        self._logger = logger

    def register(self, command_class: Type[Command], handler: CommandHandler):
        self._guard_has_been_called()
        self._mapping[command_class] = handler

    def dispatch(self, command: Command):
        self._mark_as_asked()
        handler = self._get_handler(command)
        return handler(command)

    def is_sync(self):
        return self._IS_SYNC

    def _get_handler(self, command: Command):
        try:
            return self._mapping[type(command)]
        except KeyError as e:
            self._logger.critical(f'Command "%s" has not been registered.', type(command).__name__)
            raise CommandNotRegisteredError from e

    def _guard_has_been_called(self):
        if self._ask_has_been_called:
            raise CommandRegisteredAfterDispatch('Trying to register a new handler after some command has been dispatched')

    def _mark_as_asked(self):
        self._ask_has_been_called = True

