from abc import ABC, abstractmethod

from context.shared.domain.bus.command.command import Command


class CommandBus(ABC):
    @abstractmethod
    def dispatch(self, command: Command):
        pass

    @abstractmethod
    def is_sync(self) -> bool:
        pass
