import re

from context.i18n.shared.domain.abstract.subtag_field import SubtagField


class ScriptSubtag(SubtagField):
    _REGEXP_PATTERN = re.compile("^[A-Z][a-z]{3}$")

    @classmethod
    def regexp_pattern(cls) -> re.Pattern:
        return cls._REGEXP_PATTERN
