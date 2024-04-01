import dataclasses
from typing import Optional

from context.shared.domain.bus.request.request_account_schema import RequestAccountSchema


@dataclasses.dataclass(frozen=True, kw_only=True)
class RequestMetadataSchema:
    request_id: str
    account: Optional[RequestAccountSchema]
