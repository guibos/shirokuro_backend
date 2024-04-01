from context.shared.domain.types.var_char_type import VarCharType


class CommentValue(VarCharType):
    """A value of :class:`context.i18n.shared.domain.value_object.comments.Comments`"""
    _MIN_LENGTH = 1
    _MAX_LENGTH = 1

    @classmethod
    def min_length(cls):
        return cls._MIN_LENGTH

    @classmethod
    def max_length(cls):
        return cls._MAX_LENGTH
