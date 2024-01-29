from context.user.account.domain.aggregate.account import Account
from context.user.account.domain.repository.account_repository_interface import AccountRepositoryInterface


class AccountRepositoryKeyCloak(AccountRepositoryInterface):
    def create(self, account: Account) -> None:
        pass
