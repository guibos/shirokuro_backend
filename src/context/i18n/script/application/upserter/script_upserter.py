from logging import Logger
from typing import Set, List

from context.i18n.script.application.upserter.script_upserter_command_data import ScriptUpserterCommandData
from context.i18n.script.domain.aggregate.script import Script
from context.i18n.script.domain.repository.script_repository import ScriptRepository
from context.shared.application.application.application_command import ApplicationCommand
from context.shared.domain.value_types.request_metadata.request_metadata import RequestMetadata
from context.shared.domain.value_types.role.role_name import RoleName


class ScriptUpserter(ApplicationCommand):
    _REQUIRED_ROLES = {RoleName('script:write')}

    def __init__(self, logger: Logger, event_bus, script_repository: ScriptRepository):
        self._script_repository = script_repository
        super().__init__(logger, event_bus)

    async def _command(self, scripts_common: List[ScriptUpserterCommandData], metadata: RequestMetadata):
        scripts_entities = [Script.create(script_common) for script_common in scripts_common]
        await self._script_repository.upsert(scripts_entities)

    @property
    def _required_roles(self) -> Set[RoleName]:
        return self._REQUIRED_ROLES
