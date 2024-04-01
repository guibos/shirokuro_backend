import dataclasses

from context.internationalization.script.domain.value_object.script_subtag import ScriptSubtag
from context.internationalization.shared.domain.abstract.subtag import Subtag
from context.internationalization.shared.domain.value_object.comments import Comments
from context.shared.domain.aggregate.aggregate_root import AggregateRoot


@dataclasses.dataclass
class Script(AggregateRoot, Subtag):
    """Script subtags are used to indicate the script or writing system variations that distinguish the written forms of
    a language or its dialects.

    For more information: https://www.rfc-editor.org/rfc/bcp/bcp47.txt"""
    subtag: ScriptSubtag
    comments: Comments
