from context.shared.application.application.application_command import ApplicationCommand
from context.shared.domain.bus.command.command import Command
from context.shared.domain.bus.command.handler.command_handler import CommandHandler


class CommandHandlerSync(CommandHandler):

    def __init__(self, app: ApplicationCommand) -> None:
        self._app = app

    async def handle(self, command: Command):
        await self._app.command(command)
