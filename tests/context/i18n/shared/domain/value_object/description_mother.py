import random
from typing import List

from context.i18n.shared.domain.value_object.description_value import DescriptionValue
from tests.context.i18n.shared.domain.value_object.description_value_mother import description_value_mother


class _DescriptionMother:
    _MAX_ITEMS = 10

    def random(self) -> List[DescriptionValue]:
        i = random.randint(0, self._MAX_ITEMS)
        return [description_value_mother.random() for _ in range(i)]

    def random_max(self) -> List[DescriptionValue]:
        i = random.randint(0, self._MAX_ITEMS)
        return [description_value_mother.random_max() for _ in range(i)]

    def random_min(self) -> List[DescriptionValue]:
        i = random.randint(0, self._MAX_ITEMS)
        return [description_value_mother.random_max() for _ in range(i)]


description_mother = _DescriptionMother()
