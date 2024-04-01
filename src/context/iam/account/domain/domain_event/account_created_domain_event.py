from typing import Optional

from context.shared.domain.bus.event.domain_event import DomainEvent


class AccountCreatedDomainEvent(DomainEvent):
    _EVENT_NAME = "User.created"

    def __init__(self,
                 account_id: str,
                 username: str,
                 email: str,
                 password: str,
                 event_id: Optional[str] = None,
                 occurred_on: Optional[str] = None) -> None:
        self._username = username
        self._email = email
        self._password = password
        super().__init__(user_id, event_id, occurred_on)

    def event_name(self) -> str:
        return self._EVENT_NAME

    @classmethod
    def from_primitive(
            cls, aggregate_id: str, body: Dict[str,
            Any], event_id: Optional[str],
            occurred_on: Optional[str]) -> 'AccountCreatedDomainEvent':
        return cls(aggregate_id, body['username'], body['email'],
                   body['password'], event_id, occurred_on)

    def to_primitives(self) -> Dict[str, Any]:
        return {
            'username': self._username,
            'email': self._email,
            'password': self._password
        }
