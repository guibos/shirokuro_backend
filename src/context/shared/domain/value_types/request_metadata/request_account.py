import dataclasses
from typing import Set

from context.shared.domain.value_types.account.account_id import AccountId
from context.shared.domain.value_types.role.role_name import RoleName


@dataclasses.dataclass(frozen=True, kw_only=True)
class RequestAccount:
    account_id: AccountId
    roles: Set[RoleName]
