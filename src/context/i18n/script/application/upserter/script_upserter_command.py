import dataclasses
from typing import List

from context.i18n.script.application.upserter.script_upserter_command_data import ScriptUpserterCommandData
from context.shared.domain.bus.command.command import Command


@dataclasses.dataclass(frozen=True, kw_only=True)
class ScriptUpserterCommand(Command):
    data: List[ScriptUpserterCommandData]
