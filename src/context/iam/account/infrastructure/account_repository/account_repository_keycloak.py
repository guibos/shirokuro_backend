from context.iam.account.domain.aggregate.account import Account
from context.iam.account.domain.repository.account_repository_interface import AccountRepositoryInterface


class AccountRepositoryKeyCloak(AccountRepositoryInterface):
    def create(self, account: Account) -> None:
        pass
