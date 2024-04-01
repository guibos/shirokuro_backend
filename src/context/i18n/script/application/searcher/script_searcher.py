import logging
from typing import Set

from context.i18n.script.application.searcher.script_searcher_query import ScriptSearcherQuery
from context.i18n.script.domain.repository.script_repository import ScriptRepository
from context.shared.application.application.application_query import ApplicationQuery
from context.shared.domain.bus.event.event_bus import EventBus
from context.shared.domain.bus.query.response import Response
from context.shared.domain.value_types.request_metadata.request_metadata import RequestMetadata
from context.shared.domain.value_types.role.role_name import RoleName


class ScriptSearcher(ApplicationQuery):
    _REQUIRED_ROLES = set()

    def __init__(self, logger: logging.Logger, event_bus: EventBus, script_repository: ScriptRepository):
        super().__init__(logger, event_bus)
        self._script_repository = script_repository

    async def _query(self, query_data: ScriptSearcherQuery, metadata: RequestMetadata) -> Response:
        pass

    def _required_roles(self) -> Set[RoleName]:
        return self._REQUIRED_ROLES
