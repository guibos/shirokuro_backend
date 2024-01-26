from abc import ABC, abstractmethod

from context.user.domain.aggreagate.user import User
from context.user.domain.value_object.user_id import UserId


class UserRepositoryInterface(ABC):
    def create_user_id(self) -> UserId:
        pass

    @abstractmethod
    def create(self, user: User) -> None:
        pass
