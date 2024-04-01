import logging
from abc import ABC, abstractmethod
from typing import Set

from context.shared.domain.bus.event.event_bus import EventBus
from context.shared.domain.bus.request.request_metadata_schema import RequestMetadataSchema
from context.shared.domain.exception.security.child.forbidden_error import ForbiddenError
from context.shared.domain.value_types.account.account_id import AccountId
from context.shared.domain.value_types.request_metadata.request_account import RequestAccount
from context.shared.domain.value_types.request_metadata.request_id import RequestId
from context.shared.domain.value_types.request_metadata.request_metadata import RequestMetadata
from context.shared.domain.value_types.role.role_name import RoleName


class Application(ABC):
    _FULL_ACCESS_ROLE = 'full:access'

    def __init__(self, logger: logging.Logger, event_bus: EventBus):
        self._logger = logger
        self._event_bus = event_bus

    @staticmethod
    def _get_request_metadata_value_object(request_metadata_schema: RequestMetadataSchema) -> RequestMetadata:
        return RequestMetadata(
            request_id=RequestId(request_metadata_schema.request_id),
            account=RequestAccount(
                account_id=AccountId(request_metadata_schema.account.account_id),
                roles={RoleName(role_name) for role_name in request_metadata_schema.account.roles},
            )
        )

    async def _check_roles(self, request_metadata: RequestMetadata) -> None:
        if self._FULL_ACCESS_ROLE in request_metadata.account.roles:
            return
        elif missing_roles := request_metadata.account.roles.difference(self._required_roles):
            raise ForbiddenError(request_metadata.account.account_id, missing_roles)

    @property
    @abstractmethod
    def _required_roles(self) -> Set[RoleName]:
        raise NotImplementedError

    @property
    def application_name(self):
        return self.__class__.__name__
