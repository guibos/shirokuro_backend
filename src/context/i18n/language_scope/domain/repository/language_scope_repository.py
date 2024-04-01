from abc import ABC, abstractmethod
from typing import List

from context.i18n.language_scope.domain.aggregate.lanaguage_scope import LanguageScope


class LanguageScopeRepository(ABC):

    @abstractmethod
    def search(self) -> List[LanguageScope]:
        raise NotImplementedError

    @abstractmethod
    def create(self, language_scope: LanguageScope) -> None:
        raise NotImplementedError
