import dataclasses

from context.user.account.domain.domain_event.account_created_domain_event import AccountCreatedDomainEvent
from context.user.account.domain.value_object import AccountId
from context.user.account.domain.value_object import Email
from context.user.account.domain.value_object.password import Password
from context.user.account.domain.value_object.username import Username
from context.shared.domain.aggregate.aggregate_root import AggregateRoot


@dataclasses.dataclass
class Account(AggregateRoot):
    account_id: AccountId
    username: Username
    email: Email
    password: Password

    @classmethod
    def create(cls, account_id: AccountId, username: Username, email: Email, password: Password) -> 'Account':
        account = Account(
            account_id=account_id,
            username=username,
            email=email,
            password=password,
        )

        account._record(
            AccountCreatedDomainEvent
        )

        return account