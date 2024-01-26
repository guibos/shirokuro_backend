import dataclasses


@dataclasses.dataclass(frozen=True)
class CommandMeta:
    request_id: str
    request_timestamp: str
