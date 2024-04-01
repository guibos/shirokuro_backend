from abc import ABC

from context.shared.domain.bus.request.request import Request


class Query(Request, ABC):
    pass
