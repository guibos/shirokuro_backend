import dataclasses


@dataclasses.dataclass(frozen=True, kw_only=True)
class ResponseErrorData:
    internal: bool
    message: str
    traceback: str
