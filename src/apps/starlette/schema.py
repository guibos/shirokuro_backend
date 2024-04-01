import typing
import uuid

import strawberry

from apps.starlette.i18n.entity.script.script_type import ScriptType
from context.i18n.script.domain.aggregate.script import Script


def get_scripts():
    return [
        ScriptType(id=uuid.uuid4()),
    ]


@strawberry.type
class Query:
    scripts: typing.List[ScriptType] = strawberry.field(resolver=get_scripts, description=Script.__doc__)


schema = strawberry.Schema(query=Query)
