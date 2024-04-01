from abc import ABC, abstractmethod
from typing import Any

from context.shared.application.application.application import Application
from context.shared.domain.bus.command.command import Command
from context.shared.domain.exception.internal.child.unexpected_error import UnexpectedError
from context.shared.domain.value_types.request_metadata.request_metadata import RequestMetadata


class ApplicationCommand(Application, ABC):
    async def command(self, command: Command) -> None:

        try:
            request_metadata = self._get_request_metadata_value_object(command.request_metadata)
            await self._check_roles(request_metadata)
            return await self._command(command.data, request_metadata)
        except Exception as e:
            raise UnexpectedError from e

    @abstractmethod
    async def _command(self, command_data: Any, metadata: RequestMetadata) -> None:
        raise NotImplementedError
