"""Module that contains BaseType abstract."""
import abc
import dataclasses
from abc import ABC


from context.internationalization.shared.domain.value_object.created_at import CreatedAt
from context.internationalization.shared.domain.value_object.description import Description
from context.internationalization.shared.domain.value_object.tag import Tag
from context.internationalization.shared.domain.value_object.updated_at import UpdatedAt
from context.shared.domain.types.id import Id


@dataclasses.dataclass
class BaseType(ABC):
    """Mixin that must be used by all BCP47 types. Only contains fields that are common between all BCP47 types."""
    id: Id
    description: Description
    created_at: CreatedAt
    updated_at: UpdatedAt

    @property
    @abc.abstractmethod
    def tag(self) -> Tag:  # TODO
        """Return the string tag. If only have a subtag return the subtag."""
