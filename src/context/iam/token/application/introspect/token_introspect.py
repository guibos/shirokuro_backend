class TokenIntrospect:
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