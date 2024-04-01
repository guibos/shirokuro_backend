import typing
from datetime import datetime

import strawberry

from context.i18n.script.domain.value_object.script_subtag import ScriptSubtag
from context.i18n.shared.domain.value_object.comment import Comment
from context.shared.domain.value_types.common.created_at import CreatedAt
from context.i18n.shared.domain.value_object.description import Description
from context.shared.domain.value_types.common.updated_at import UpdatedAt


@strawberry.type
class ScriptType:
    """test caca """
    subtag: str = strawberry.field(description=ScriptSubtag.__doc__)
    description: typing.List[str] = strawberry.field(description=Description.__doc__)
    comment: typing.List[str] = strawberry.field(description=Comment.__doc__)
    created_at: datetime = strawberry.field(description=CreatedAt.__doc__)
    updated_at: datetime = strawberry.field(description=UpdatedAt.__doc__)
