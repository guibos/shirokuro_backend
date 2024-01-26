from context.account.domain.aggregate.account import Account
from context.account.domain.repository.account_repository_interface import AccountRepositoryInterface


class AccountRepositoryPostgres(AccountRepositoryInterface):
    def create(self, account: Account) -> None:
        pass
