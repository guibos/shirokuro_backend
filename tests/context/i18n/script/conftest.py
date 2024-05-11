from typing import List

from context.i18n.script.domain.aggregate.script import Script
from context.i18n.script.domain.repository.script_repository import ScriptRepository
from context.shared.domain.criteria.criteria import Criteria


class ScriptRepositoryMocked(ScriptRepository):
    async def search(self, criteria: Criteria) -> List[Script]:
        pass

    async def upsert(self, scripts: List[Script]) -> None:
        pass
