"""Module that contains Subtag abstract class."""
import dataclasses
from abc import ABC, abstractmethod

from context.i18n.shared.domain.abstract.bcp47_base import BCP47Base
from context.i18n.shared.domain.abstract.subtag_field import SubtagField


@dataclasses.dataclass(kw_only=True)
class BCP47Subtag(BCP47Base, ABC):
    """Mixin that must be used by subtag types (all except :class:`schemas.redundant.Redundant` and
    :class:`grandfathered.Grandfathered` types)."""
    subtag: SubtagField

    @property
    def tag(self) -> str:
        return str(self.subtag)
