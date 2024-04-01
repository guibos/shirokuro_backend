import dataclasses

from context.i18n.script.application.upserter.script_upserter_command_data import ScriptUpserterCommandData
from context.i18n.script.domain.value_object.script_subtag import ScriptSubtag
from context.i18n.shared.domain.abstract.subtag import BCP47Subtag
from context.i18n.shared.domain.value_object.comment import Comment
from context.i18n.shared.domain.value_object.comment_value import CommentValue
from context.shared.domain.value_types.common.created_at import CreatedAt
from context.i18n.shared.domain.value_object.description import Description
from context.i18n.shared.domain.value_object.description_value import DescriptionValue
from context.shared.domain.value_types.common.updated_at import UpdatedAt


@dataclasses.dataclass(kw_only=True)
class Script(BCP47Subtag):
    """Script subtags are used to indicate the script or writing system variations that distinguish the written forms of
    a language or its dialects.

    For more information: https://www.rfc-editor.org/rfc/bcp/bcp47.txt"""
    subtag: ScriptSubtag
    comment: Comment

    @classmethod
    def create(cls, script_command: ScriptUpserterCommandData) -> 'Script':
        # NO domain event required
        return cls(
            subtag=ScriptSubtag(script_command.subtag),
            comment=Comment([CommentValue(comment_value) for comment_value in script_command.comment]),
            description=Description(
                [DescriptionValue(description_value) for description_value in script_command.description]),
            created_at=CreatedAt.from_datetime(script_command.created_at),
            updated_at=UpdatedAt.from_datetime(script_command.updated_at),
        )
