import dataclasses
from abc import ABC

from context.shared.domain.bus.request.request import Request


@dataclasses.dataclass(frozen=True, kw_only=True)
class Command(Request, ABC):
    pass
