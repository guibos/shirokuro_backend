import dataclasses
from abc import ABC
from typing import List, Any

from context.shared.domain.bus.query.response_error_data import ResponseErrorData


@dataclasses.dataclass(frozen=True, kw_only=True)
class Response(ABC):
    ok: bool
    errors: List[ResponseErrorData]
    data: List[Any]
