from context.shared.domain.bus.command.command_handler import CommandHandler
from context.user.application.creator.user_creator import UserCreator
from context.user.application.creator.user_creator_command import UserCreatorCommand
from context.user.domain.value_object.email import Email
from context.user.domain.value_object.password import Password
from context.user.domain.value_object.user_id import UserId
from context.user.domain.value_object.username import Username


class UserCreatorCommandHandler(CommandHandler):
    def __init__(self, user_creator: UserCreator):
        self._user_creator = user_creator

    def __call__(self, command: UserCreatorCommand) -> None:
        self._user_creator.create(
            user_id=UserId(command.user_id),
            username=Username(command.username),
            password=Password(command.password),
            email=Email(command.email)
        )
