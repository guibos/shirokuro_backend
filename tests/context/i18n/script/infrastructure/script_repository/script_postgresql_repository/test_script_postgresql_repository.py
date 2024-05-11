from typing import List

import pytest

from context.boundary_context import BoundaryContext
from context.i18n.script.domain.aggregate.script import Script
from context.i18n.script.infrastructure.script_repository.script_postgresql_repository.script_postgresql_repository import \
    ScriptPostgresqlRepository
from tests.conftest import DatabaseConfiguration
from tests.context.i18n.script.domain.aggregate.script_mother import ScriptMother


mother = ScriptMother()
test_cases_large = [mother.random() for _ in range(5000)]


@pytest.mark.parametrize('new_database_migrated', [[BoundaryContext.I18N]],
                         indirect=['new_database_migrated'])
@pytest.mark.parametrize('test_case', ScriptMother().test_cases())
async def test_create_one(new_database_migrated: DatabaseConfiguration, test_case: Script):
    repo = ScriptPostgresqlRepository(new_database_migrated.session_maker)
    await repo.upsert([test_case])


@pytest.mark.parametrize('new_database_migrated', [[BoundaryContext.I18N]],
                         indirect=['new_database_migrated'])
async def test_create_many(new_database_migrated: DatabaseConfiguration):
    repo = ScriptPostgresqlRepository(new_database_migrated.session_maker)
    test_cases = ScriptMother().test_cases()
    await repo.upsert(test_cases)


@pytest.mark.parametrize('new_database_migrated', [[BoundaryContext.I18N]],
                         indirect=['new_database_migrated'])
@pytest.mark.parametrize('test_cases', [test_cases_large])
async def test_create_performance(new_database_migrated: DatabaseConfiguration, test_cases: List[Script]):
    repo = ScriptPostgresqlRepository(new_database_migrated.session_maker)
    await repo.upsert(test_cases)
