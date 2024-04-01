import dataclasses

from context.i18n.language_scope.domain.enum.scope import Scope
from context.i18n.language_scope.domain.value_object.language_scope_id import LanguageScopeId
from context.shared.domain.aggregate.aggregate_root import AggregateRoot


@dataclasses.dataclass
class LanguageScope(AggregateRoot):
    id: LanguageScopeId
    scope: Scope
