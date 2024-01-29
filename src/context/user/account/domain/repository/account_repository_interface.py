from abc import ABC

from context.user.account.domain.aggregate.account import Account


class AccountRepositoryInterface(ABC):

    def create_account(self, account: Account) -> None:
        pass
