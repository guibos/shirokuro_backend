import dataclasses

from context.shared.domain.value_types.request_metadata.request_account import RequestAccount
from context.shared.domain.value_types.request_metadata.request_id import RequestId


@dataclasses.dataclass(frozen=True, kw_only=True)
class RequestMetadata:
    request_id: RequestId
    account: RequestAccount
