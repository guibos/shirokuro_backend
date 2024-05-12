from context.shared.domain.types.datetime_type import DatetimeType
from tests.context.shared.domain.types.datetime_type_mother_base import DatetimeTypeMotherBase

class TestDatetime(DatetimeType):
    pass


def test_datetime_type_mother_base():
    mother = DatetimeTypeMotherBase(TestDatetime)
    test1 = mother.random()
    test2 = mother.random()

    assert isinstance(test1, DatetimeTypeMotherBase)
    assert test1 != test2
