from context.iam.account.application.creator.account_creator import AccountCreator
from context.iam.account.application.creator.account_creator_command import AccountCreatorCommand
from context.shared.domain.bus.command.command_handler import CommandHandler
from context.iam.domain.value_object.email import Email
from context.iam.domain.value_object.password import Password
from context.iam.domain.value_object.username import Username


class AccountCreatorCommandHandler(CommandHandler):
    def __init__(self, account_creator: AccountCreator):
        self._account_creator = account_creator

    def __call__(self, command: AccountCreatorCommand) -> None:
        self._account_creator.create(
            user_id=command.user_id,
            username=Username(command.username),
            password=Password(command.password),
            email=Email(command.email)
        )