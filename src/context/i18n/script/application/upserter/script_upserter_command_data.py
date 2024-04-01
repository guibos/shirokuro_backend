import dataclasses

from context.i18n.script.application.shared.script_common import ScriptCommon


@dataclasses.dataclass(frozen=True, kw_only=True)
class ScriptUpserterCommandData(ScriptCommon):
    pass
