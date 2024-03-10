from context.iam.account.domain.value_object.password import Password
from tests.context.shared.domain.types.varchar_type_mother_base import VarcharTypeMotherBase


class PasswordMother(VarcharTypeMotherBase, Password):
    def create(self) -> Password:
        return Password(self._get_random_string())
