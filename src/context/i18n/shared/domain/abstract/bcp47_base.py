"""Module that contains BaseType abstract."""
import abc
import dataclasses
from abc import ABC

from context.shared.domain.value_types.common.created_at import CreatedAt
from context.i18n.shared.domain.value_object.description import Description
from context.i18n.shared.domain.value_object.tag import Tag
from context.shared.domain.value_types.common.updated_at import UpdatedAt
from context.shared.domain.aggregate.aggregate_root import AggregateRoot


@dataclasses.dataclass(kw_only=True)
class BCP47Base(AggregateRoot, ABC):
    """Mixin that must be used by all BCP47 types. Only contains fields that are common between all BCP47 types."""
    description: Description
    created_at: CreatedAt
    updated_at: UpdatedAt

    @property
    @abc.abstractmethod
    def tag(self) -> Tag:
        """Return the string tag. If only have a subtag return the subtag."""
