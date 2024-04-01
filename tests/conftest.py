import uuid
from dataclasses import dataclass
from typing import List

import pytest
from _pytest.fixtures import SubRequest
from dotenv import dotenv_values
from pytest_docker_tools import container
from pytest_docker_tools.wrappers import Container
from sqlalchemy import URL, text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from apps.migrate.main import migrate
from context.boundary_context import BoundaryContext

_CONFIG = dotenv_values(".template.env")

_database_container = container(image=_CONFIG["DATABASE_IMAGE"],
                                environment={
                                    'POSTGRES_USER': _CONFIG["DATABASE_USER"],
                                    'POSTGRES_PASSWORD': _CONFIG["DATABASE_PASS"],
                                    'POSTGRES_DB': _CONFIG["DATABASE_NAME"],
                                },
                                ports={
                                        _CONFIG["DATABASE_PORT"]: None,
                                },

            )


@dataclass(frozen=True)
class DatabaseConfiguration:
    url: URL
    session_maker: async_sessionmaker


@pytest.fixture(scope="function")
async def new_database_configuration(_database_container: Container) -> DatabaseConfiguration:
    new_database_name = f"db_{uuid.uuid4().hex}"
    default_url = URL.create(
        drivername="postgresql+asyncpg",
        host='localhost',
        port=_database_container.ports['5432/tcp'][0],
        username=_database_container.env["POSTGRES_USER"],
        password=_database_container.env["POSTGRES_PASSWORD"],
        database=_database_container.env["POSTGRES_DB"],
    )
    default_engine = create_async_engine(default_url)
    default_async_session_maker = async_sessionmaker(default_engine)
    async with default_async_session_maker() as session:
        await session.execute(text("commit"))
        await session.execute(text(f"CREATE DATABASE {new_database_name}"))
        await session.commit()
        await session.flush()
    await default_engine.dispose(close=True)
    new_url = URL.create(
        drivername=default_url.drivername,
        host=default_url.host,
        port=default_url.port,
        username=default_url.username,
        password=default_url.password,
        database=new_database_name,
    )
    new_engine = create_async_engine(new_url)
    new_async_session_maker = async_sessionmaker(new_engine)

    return DatabaseConfiguration(
        url=new_url,
        session_maker=new_async_session_maker,
    )


@pytest.fixture(scope="function")
async def new_database_migrated(
        new_database_configuration: DatabaseConfiguration,
        request: SubRequest) -> DatabaseConfiguration:
    boundary_contexts: List[BoundaryContext] = request.param
    await migrate(boundary_contexts, new_database_configuration.url)
    return new_database_configuration
