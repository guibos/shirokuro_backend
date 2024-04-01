from typing import List

from sqlalchemy.ext.asyncio import async_sessionmaker

from context.i18n.language_scope.domain.aggregate.lanaguage_scope import LanguageScope
from context.i18n.language_scope.domain.repository.language_scope_repository import LanguageScopeRepository
from context.i18n.language_scope.infrastructure.language_scope_repository.language_scope_database_repository.models.language_scope_model import \
    LanguageScopeModel


class LanguageScopeDatabaseRepository(LanguageScopeRepository):
    def __init__(self, session_maker: async_sessionmaker):
        self._session_maker = session_maker

    def search(self) -> List[LanguageScope]:
        pass

    def create(self, language_scope: LanguageScope) -> None:
        async with self._session_maker() as session:
            async with session.begin():
                session.add(LanguageScopeModel.from_aggregate(language_scope))
