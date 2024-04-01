from sqlalchemy import Column, VARCHAR

from context.i18n.language_scope.domain.aggregate.lanaguage_scope import LanguageScope
from context.i18n.language_scope.domain.enum.scope import Scope
from context.i18n.language_scope.domain.value_object.language_scope_id import LanguageScopeId
from context.i18n.shared.infrastructure.database.models.base_i18n_model import BaseI18nModel


class LanguageScopeModel(BaseI18nModel):
    __tablename__ = "language_scope"
    scope = Column(VARCHAR(13), unique=True, nullable=False)

    @classmethod
    def from_aggregate(cls,
                       language_scope: LanguageScope) -> "LanguageScopeModel":
        return LanguageScopeModel(id=language_scope.id,
                                  scope=language_scope.scope.value)

    def to_aggregate(self) -> LanguageScope:
        return LanguageScope(id=LanguageScopeId(self.id),
                             scope=Scope(self.scope))
