import dataclasses
from abc import ABC, abstractmethod
from typing import Any

from context.shared.domain.bus.request.request_metadata_schema import RequestMetadataSchema


@dataclasses.dataclass(frozen=True, kw_only=True)
class Request(ABC):
    request_metadata: RequestMetadataSchema

    @property
    @abstractmethod
    def data(self) -> Any:
        raise NotImplementedError
