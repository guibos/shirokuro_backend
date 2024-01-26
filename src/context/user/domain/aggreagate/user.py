import dataclasses

from context.shared.domain.aggregate.aggregate_root import AggregateRoot
from context.user.domain.domain_events.user_created_domain_event import UserCreatedDomainEvent
from context.user.domain.value_object.email import Email
from context.user.domain.value_object.password import Password
from context.user.domain.value_object.user_id import UserId
from context.user.domain.value_object.username import Username


@dataclasses.dataclass
class User(AggregateRoot):
    user_id: UserId
    username: Username
    email: Email
    password: Password

    @classmethod
    def create(cls, user_id: UserId, username: Username, email: Email, password: Password) -> 'User':
        # TODO primitives
        user = User(user_id=user_id, username=username, email=email, password=password)
        user._record(UserCreatedDomainEvent)
