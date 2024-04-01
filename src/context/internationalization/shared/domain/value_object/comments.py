from typing import Iterable

from context.internationalization.shared.domain.value_object.comment import Comment


class Comments(list):
    """The field 'Comments' contains additional information about the record and MAY appear more than once
    per record. The field-body MAY include the full range of Unicode characters and is not restricted to any
    particular script. This field MAY be inserted or changed via the registration process, and no guarantee of
    stability is provided."""
    def __init__(self, iterable: Iterable[Comment]) -> None:
        for item in iterable:
            if not isinstance(item, Comment):
                raise TypeError(f"Invalid type: {type(item)}")

        super().__init__(iterable)

    def __setitem__(self, index: int, item: Comment):
        if not isinstance(item, Comment):
            raise TypeError(f'Invalid type to setitem: {type(item)}')
        super().__setitem__(index, str(item))

    def insert(self, index: int, item: Comment):
        if not isinstance(item, Comment):
            raise TypeError(f'Invalid type to insert: {type(item)}')
        super().insert(index, str(item))

    def append(self, item: Comment):
        if not isinstance(item, Comment):
            raise TypeError(f'Invalid type to append: {type(item)}')
        super().append(item)

    def extend(self, other: 'Comments'):
        if not isinstance(other, type(self)):
            raise TypeError(f'Invalid type to extend: {type(other)}')
        super().extend(other)