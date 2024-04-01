import dataclasses
from typing import List

from context.i18n.shared.application.abstract.subtag_common import SubtagCommon


@dataclasses.dataclass(frozen=True, kw_only=True)
class ScriptCommon(SubtagCommon):
    comment: List[str]
