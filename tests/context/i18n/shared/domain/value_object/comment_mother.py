import random
from typing import List

from context.i18n.shared.domain.value_object.comment_value import CommentValue
from tests.context.i18n.shared.domain.value_object.comment_value_mother import comment_value_mother


class _CommentMother:
    _MAX_ITEMS = 10

    def random(self) -> List[CommentValue]:
        i = random.randint(0, self._MAX_ITEMS)
        return [comment_value_mother.random() for _ in range(i)]

    def random_max(self) -> List[CommentValue]:
        i = random.randint(0, self._MAX_ITEMS)
        return [comment_value_mother.random_max() for _ in range(i)]

    def random_min(self) -> List[CommentValue]:
        i = random.randint(0, self._MAX_ITEMS)
        return [comment_value_mother.random_min() for _ in range(i)]


comment_mother = _CommentMother()
