import dataclasses
from abc import ABC

from context.i18n.shared.application.abstract.bcp47_base_common import BCP47BaseCommon


@dataclasses.dataclass(frozen=True, kw_only=True)
class SubtagCommon(BCP47BaseCommon, ABC):
    subtag: str
