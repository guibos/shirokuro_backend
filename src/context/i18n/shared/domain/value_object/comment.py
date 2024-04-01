from typing import Iterable

from context.i18n.shared.domain.value_object.comment_value import CommentValue


class Comment(list):
    """The field 'Comments' contains additional information about the record and MAY appear more than once
    per record. The field-body MAY include the full range of Unicode characters and is not restricted to any
    particular script. This field MAY be inserted or changed via the registration process, and no guarantee of
    stability is provided."""

    def __init__(self, iterable: Iterable[CommentValue]) -> None:
        for item in iterable:
            if not isinstance(item, CommentValue):
                raise TypeError(f"Invalid type: {type(item)}")

        super().__init__(iterable)

    def __setitem__(self, index: int, item: CommentValue):
        if not isinstance(item, CommentValue):
            raise TypeError(f'Invalid type to setitem: {type(item)}')
        super().__setitem__(index, str(item))

    def insert(self, index: int, item: CommentValue):
        if not isinstance(item, CommentValue):
            raise TypeError(f'Invalid type to insert: {type(item)}')
        super().insert(index, str(item))

    def append(self, item: CommentValue):
        if not isinstance(item, CommentValue):
            raise TypeError(f'Invalid type to append: {type(item)}')
        super().append(item)

    def extend(self, other: 'Comment'):
        if not isinstance(other, type(self)):
            raise TypeError(f'Invalid type to extend: {type(other)}')
        super().extend(other)
