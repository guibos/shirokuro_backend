from logging import Logger
from typing import Set

from context.i18n.migrate.application.i18n_migrator_command import I18nMigratorCommand
from context.shared.application.application.application_command import ApplicationCommand
from context.shared.domain.bus.event.event_bus import EventBus
from context.shared.domain.value_types.request_metadata.request_metadata import RequestMetadata
from context.shared.domain.value_types.role.role_name import RoleName


class I18nMigrator(ApplicationCommand):
    _REQUIRED_ROLES = {RoleName('full:access')}

    def __init__(self, logger: Logger, event_bus: EventBus):
        super().__init__(logger, event_bus)

    def _command(self, command_data: I18nMigratorCommand, metadata: RequestMetadata) -> None:
        pass

    @property
    def _required_roles(self) -> Set[RoleName]:
        return self._REQUIRED_ROLES
