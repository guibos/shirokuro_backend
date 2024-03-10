import dataclasses

from context.iam.account.application.creator.account_creator_command_data import AccountCreatorCommandData
from context.shared.domain.bus.command.command import Command


@dataclasses.dataclass(frozen=True, kw_only=True)
class AccountCreatorCommand(Command):
    data: AccountCreatorCommandData
