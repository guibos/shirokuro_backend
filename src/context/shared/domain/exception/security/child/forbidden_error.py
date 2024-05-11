from typing import Set

from context.shared.domain.exception.security.security_base_error import SecurityBaseError
from context.shared.domain.value_types.account.account_id import AccountId
from context.shared.domain.value_types.role.role_name import RoleName


class ForbiddenError(SecurityBaseError):
    _PRIVATE_MESSAGE_TEMPLATE = 'Forbidden. User "{}" tried to access to "{}" missing following roles: {}'
    _PUBLIC_MESSAGE_TEMPLATE = 'Forbidden.'

    def __init__(self, account_id: AccountId, application: str, roles: Set[RoleName]):
        private_message = self._PRIVATE_MESSAGE_TEMPLATE.format(str(account_id), str(application),
                                                       f'''"{'", "'.join(roles)}"''')
        super().__init__(
            private_message=private_message,
            public_message=self._PUBLIC_MESSAGE_TEMPLATE,
            value=None,
            location=[]
        )
