from sqlalchemy import Column, ARRAY, VARCHAR, CHAR

from context.i18n.script.domain.aggregate.script import Script
from context.i18n.script.domain.value_object.script_subtag import ScriptSubtag
from context.i18n.shared.domain.value_object.comment import Comment
from context.i18n.shared.domain.value_object.comment_value import CommentValue
from context.shared.domain.value_types.common.created_at import CreatedAt
from context.i18n.shared.domain.value_object.description import Description
from context.i18n.shared.domain.value_object.description_value import DescriptionValue
from context.shared.domain.value_types.common.updated_at import UpdatedAt
from context.i18n.shared.infrastructure.database.models.base_i18n_subtag_model import BaseI18nSubtagModel


class ScriptModel(BaseI18nSubtagModel):
    __tablename__ = "script"
    comment = Column(ARRAY(VARCHAR(1)), nullable=False)
    subtag = Column(CHAR(4), nullable=False, primary_key=True)

    @classmethod
    def from_aggregate(cls, script: Script) -> 'ScriptModel':
        return cls(
            description=[str(description) for description in script.description],
            created_at=script.created_at.to_datetime(),
            updated_at=script.updated_at.to_datetime(),
            subtag=str(script.subtag),
            comment=[str(comment) for comment in script.comment],
        )

    def to_aggregate(self) -> Script:
        return Script(
            description=Description([
                DescriptionValue(description) for description in self.description
            ]),
            created_at=CreatedAt.from_datetime(self.created_at),
            updated_at=UpdatedAt.from_datetime(self.updated_at),
            subtag=ScriptSubtag(self.subtag),
            comment=Comment(
                [CommentValue(comment) for comment in self.comment],
            ),
        )
