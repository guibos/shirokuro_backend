import dataclasses


@dataclasses.dataclass(frozen=True)
class AccountCreatorCommandData:
    account_id: str
    username: str
    email: str
    password: str
