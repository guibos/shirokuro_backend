import logging

from context.iam.account.application.creator import AccountCreator
from context.iam.account.application.creator import AccountCreatorCommand
from context.iam.account.application.creator import AccountCreatorCommandHandler
from context.iam.account.infrastructure.account_repository.account_repository_keycloak import AccountRepositoryKeyCloak
from context.shared.domain.bus.event.event_bus import EventBus
from context.shared.infrastructure.bus.command.command_bus_sync import CommandBusSync
from context.shared.infrastructure.bus.query.query_bus_sync import QueryBusSync

query_bus = QueryBusSync(logging.getLogger())
command_bus = CommandBusSync(logging.getLogger())
_event_bus = EventBus()

_account_repository = AccountRepositoryKeyCloak()

_account_creator = AccountCreator(_account_repository, _event_bus)

_account_creator_handler = AccountCreatorCommandHandler(_account_creator)

command_bus.register(AccountCreatorCommand, _account_creator_handler)

