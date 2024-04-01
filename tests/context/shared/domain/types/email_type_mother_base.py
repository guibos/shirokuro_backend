import random
import re
from typing import TypeVar, Generic, List

import rstr

from context.shared.domain.types.email_type import EmailType

_T = TypeVar('_T', bound=EmailType)


class EmailTypeMotherBase(Generic[_T]):
    _MAX_TEST_CASES = 5
    _MAX_LENGTH = 320
    _DOMAIN_EXAMPLES = [
        'españa.es',
        'TheOfficialAbsoluteLongestDomainNameRegisteredOnTheWorldWideWeb.International',
        rstr.xeger(re.compile(r"^[^\v\x00-\x1F\x7F\\]{320}$")),
    ]
    _USER = [
        'Abc',
        'Abc.123',
        'user+mailbox/department=shipping',
        "!#$%&'*+-/=?^_`.{|}~",
        "用户",
        "ಬೆಂಬಲ",
        "квіточка",
        "χρήστης",
        "Dörte",
        "коля"
    ]

    def __init__(self, klass: type[_T]) -> None:
        self._klass = klass

    def random(self) -> _T:
        domain = random.choice(self._DOMAIN_EXAMPLES)
        user = random.choice(self._USER)[:320 - (len(domain) + 1)]

        return self._klass(f"{user}@{domain}")

    def test_cases(self) -> List[_T]:
        return [self.random() for _ in range(self._MAX_TEST_CASES)]
