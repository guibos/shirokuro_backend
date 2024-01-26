from uuid import UUID

from context.shared.domain.bus.command import Command


class ImageResizerCommand(Command):
    def __init__(self, uri: str):
        self._uri = uri

    @property
    def uri(self) -> str:
        return self._uri


