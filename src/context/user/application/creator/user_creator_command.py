from context.shared.domain.bus.command.command import Command


class UserCreatorCommand(Command):
    def __init__(self, user_id: str, username: str, password: str, email: str):
        self._user_id = user_id
        self._username = username
        self._password = password
        self._email = email

    @property
    def user_id(self) -> str:
        return self._user_id

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str:
        return self._password

    @property
    def email(self) -> str:
        return self._email
