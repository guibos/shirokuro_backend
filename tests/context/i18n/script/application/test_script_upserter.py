import pytest

from context.boundary_context import BoundaryContext
from context.i18n.script.application.upserter.script_upserter import ScriptUpserter
from context.i18n.script.domain.repository.script_repository import ScriptRepository
from tests.conftest import DatabaseConfiguration


def test_create_one(repository_mocked: ScriptRepository):
    ScriptUpserter()


def test_create_many():
    pass


def test_empty():
    pass


def test_duplicates():
    pass


def test_bad_request():
    pass