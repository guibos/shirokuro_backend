"""Module that contains Subtag abstract class."""
import dataclasses

from context.internationalization.shared.domain.abstract.base_type import BaseType
from context.internationalization.shared.domain.abstract.subtag_field import SubtagField


@dataclasses.dataclass
class Subtag(BaseType):
    """Mixin that must be used by subtag types (all except :class:`schemas.redundant.Redundant` and
    :class:`grandfathered.Grandfathered` types)."""
    subtag: SubtagField

    @property
    def tag(self) -> str:
        return self.subtag
