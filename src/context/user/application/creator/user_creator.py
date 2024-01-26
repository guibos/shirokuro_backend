from context.shared.domain.bus.event.event_bus import EventBus
from context.user.domain.aggreagate.user import User
from context.user.domain.repository.user_repository_interface import UserRepositoryInterface
from context.user.domain.value_object.email import Email
from context.user.domain.value_object.password import Password
from context.user.domain.value_object.user_id import UserId
from context.user.domain.value_object.username import Username


class UserCreator:
    def __init__(self, user_repository: UserRepositoryInterface, event_bus: EventBus):
        self._user_repository = user_repository
        self._event_bus = event_bus

    def create(self, user_id: UserId, username: Username, password: Password, email: Email):
        user_id = self._user_repository.create_user_id()
        user = User.create(user_id, username, email, password)
        self._user_repository.create(user)
        self._event_bus.publish(user.pull_domain_events())
