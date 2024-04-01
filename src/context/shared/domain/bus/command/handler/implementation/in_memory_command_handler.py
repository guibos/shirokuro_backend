from context.shared.application.application.application_command import ApplicationCommand
from context.shared.domain.bus.command.command import Command
from context.shared.domain.bus.command.handler.command_handler import CommandHandler


class InMemoryCommandHandler(CommandHandler):
    def __init__(self, application: ApplicationCommand):
        self.application = application

    async def handle(self, command: Command):
        await self.application.command(command)
