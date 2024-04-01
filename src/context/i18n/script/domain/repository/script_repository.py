from abc import ABC, abstractmethod
from typing import List

from context.i18n.script.domain.aggregate.script import Script
from context.shared.domain.criteria.criteria import Criteria


class ScriptRepository(ABC):

    @abstractmethod
    async def search(self, criteria: Criteria) -> List[Script]:
        raise NotImplementedError

    @abstractmethod
    async def upsert(self, scripts: List[Script]) -> bool:
        raise NotImplementedError
