import datetime
from typing import List, Any, Dict

from sqlalchemy import or_, select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import async_sessionmaker

from context.i18n.script.domain.aggregate.script import Script
from context.i18n.script.domain.repository.script_repository import ScriptRepository
from context.i18n.script.infrastructure.script_repository.script_postgresql_repository.models.script_model import \
    ScriptModel
from context.shared.domain.criteria.criteria import Criteria


class ScriptPostgresqlRepository(ScriptRepository):

    def __init__(self, session_maker: async_sessionmaker):
        self._session_maker = session_maker

    async def search(self, criteria: Criteria) -> List[Script]:
        stmt = select(ScriptModel)
        async with self._session_maker() as session:
            scripts = [script.to_aggregate() for script in await session.execute(stmt)]
        return scripts

    async def upsert(self, scripts: List[Script]) -> None:
        infra_scripts = [self._script_to_dict(script) for script in scripts]
        stmt = insert(ScriptModel).values(infra_scripts)
        do_update_stmt = stmt.on_conflict_do_update(
            index_elements=[ScriptModel.subtag],
            set_={
                ScriptModel.comment: stmt.excluded.comment,
                ScriptModel.created_at: stmt.excluded.created_at,
                ScriptModel.updated_at: stmt.excluded.updated_at,
                ScriptModel.description: stmt.excluded.description,
            },
            where=(
                or_(
                    ScriptModel.comment != stmt.excluded.comment,
                    ScriptModel.created_at != stmt.excluded.created_at,
                    ScriptModel.description != stmt.excluded.description,
                )
            ),
        )
        async with self._session_maker() as session:
            async with session.begin():
                await session.execute(do_update_stmt)
                await session.commit()




    @staticmethod
    def _script_to_dict(script: Script) -> Dict[str, Any]:
        return {
            'description': [str(description) for description in script.description],
            'created_at': script.created_at.to_datetime(),
            'updated_at': script.created_at.to_datetime(),
            'subtag': str(script.subtag),
            'comment': [str(comment) for comment in script.comment]
        }
