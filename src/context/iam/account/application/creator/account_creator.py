from context.iam.account.domain.aggregate.account import Account
from context.iam.account.domain.repository.account_repository_interface import AccountRepositoryInterface
from context.iam.account.domain.value_object.account_id import AccountId
from context.iam.account.domain.value_object.email import Email
from context.iam.account.domain.value_object.password import Password
from context.iam.account.domain.value_object.username import Username
from context.shared.domain.bus.event.event_bus import EventBus


class AccountCreator:
    def __init__(self, account_repository: AccountRepositoryInterface, event_bus: EventBus):
        self._account_repository = account_repository
        self._event_bus = event_bus

    def create(self, *, event_id: str, account_id: str, username: str, password: str, email: str):
        # TODO: Estoy pasando los primitivos a value objects en este punto por que espero que desde los repositorios
        #  obtenga datos semanticos y no primitivos aunque despues en los eventos de dominio tenga que volverlos a
        #  convertir a primitivos.
        account_id = AccountId(account_id)
        username = Username(username)
        password = Password(password)
        email = Email(email)

        account = Account.create(account_id, username, email, password)
        self._account_repository.create_account(account)
        self._event_bus.publish(account.pull_domain_events())