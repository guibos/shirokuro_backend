import dataclasses
from typing import List


@dataclasses.dataclass
class RequestAccountSchema:
    account_id: str
    roles: List[str]
