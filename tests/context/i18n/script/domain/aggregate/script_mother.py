from typing import List

from context.i18n.script.domain.aggregate.script import Script
from context.i18n.script.domain.value_object.script_subtag import ScriptSubtag
from context.i18n.shared.domain.value_object.comment import Comment
from context.i18n.shared.domain.value_object.description import Description
from tests.context.i18n.script.domain.value_object.script_subtag_mother import script_subtag_mother
from tests.context.i18n.shared.domain.value_object.comment_mother import comment_mother
from tests.context.i18n.shared.domain.value_object.description_mother import description_mother
from tests.context.shared.domain.value_object.common.created_at_mother import created_at_mother
from tests.context.shared.domain.value_object.common.updated_at_mother import updated_at_mother


class ScriptMother:

    def __init__(self):
        self._subtags = set()

    def random(self) -> Script:
        return Script(
            subtag=self._get_free_subtag(),
            updated_at=updated_at_mother.random(),
            created_at=created_at_mother.random(),
            comment=comment_mother.random(),
            description=description_mother.random()
        )

    def random_empty_array(self) -> Script:
        return Script(
            subtag=self._get_free_subtag(),
            updated_at=updated_at_mother.random(),
            created_at=created_at_mother.random(),
            comment=Comment([]),
            description=Description([]),
        )

    def random_min(self) -> Script:
        return Script(
            subtag=self._get_free_subtag(),
            updated_at=updated_at_mother.random(),
            created_at=created_at_mother.random(),
            comment=comment_mother.random_min(),
            description=description_mother.random_min(),
        )

    def random_max(self) -> Script:
        return Script(
            subtag=self._get_free_subtag(),
            updated_at=updated_at_mother.random(),
            created_at=created_at_mother.random(),
            comment=comment_mother.random_max(),
            description=description_mother.random_max(),
        )

    def _get_free_subtag(self) -> ScriptSubtag:
        while True:
            script_subtag = script_subtag_mother.random()
            if script_subtag not in self._subtags:
                self._subtags.add(script_subtag)
                return script_subtag

    def test_cases(self) -> List[Script]:
        return [self.random(), self.random_min(), self.random_max(), self.random_empty_array()]
