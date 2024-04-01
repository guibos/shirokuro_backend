import dataclasses

from context.i18n.migrate.application.i18n_migrator_command_data import I18nMigratorCommandData
from context.shared.domain.bus.command.command import Command


@dataclasses.dataclass(frozen=True, kw_only=True)
class I18nMigratorCommand(Command):
    data: I18nMigratorCommandData
