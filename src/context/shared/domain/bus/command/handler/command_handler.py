from abc import ABC, abstractmethod

from context.shared.domain.bus.command.command import Command


class CommandHandler(ABC):

    @abstractmethod
    async def handle(self, command: Command):
        pass
