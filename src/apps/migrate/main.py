import asyncio
import os
from typing import List

from alembic import command
from alembic.config import Config
from sqlalchemy import URL

from context.boundary_context import BoundaryContext


async def migrate(boundary_contexts: List[BoundaryContext], url: URL):
    for boundary_context in boundary_contexts:
        alembic_cfg = Config('alembic.ini', ini_section=boundary_context.value)
        migration_url = url.render_as_string(
            hide_password=False).replace('postgresql+asyncpg', 'postgresql+psycopg')

        alembic_cfg.set_main_option(
            'sqlalchemy.url', migration_url
            )
        command.upgrade(alembic_cfg, 'head')


async def main() -> None:
    url = URL.create(
        drivername=os.environ['database.drivername'],
        host=os.environ['database.host'],
        port=int(os.environ['database.port']),
        username=os.environ['database.username'],
        password=os.environ['database.password'],
        database=os.environ['database.database'],
    )

    await migrate([BoundaryContext.I18N], url)


if __name__ == '__main__':
    asyncio.run(main())
