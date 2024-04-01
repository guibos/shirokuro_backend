from typing import Iterable

from context.internationalization.shared.domain.value_object.description_value import DescriptionValue


class Description(list):
    """The field 'Description' contains a description of the tag or subtag in the record. The 'Description'
    field MAY appear more than once per record.

    For more information: https://www.rfc-editor.org/rfc/bcp/bcp47.txt

    Examples:

     - ["English"]
     - ["Spanish"]
     - ["Modern Greek (1453-)"]
     - ["Bengali", "Bangla"]"""

    def __init__(self, iterable: Iterable[DescriptionValue]) -> None:
        for item in iterable:
            if not isinstance(item, DescriptionValue):
                raise TypeError(f"Invalid type: {type(item)}")

        super().__init__(iterable)

    def __setitem__(self, index: int, item: DescriptionValue):
        if not isinstance(item, DescriptionValue):
            raise TypeError(f'Invalid type to setitem: {type(item)}')
        super().__setitem__(index, str(item))

    def insert(self, index: int, item: DescriptionValue):
        if not isinstance(item, DescriptionValue):
            raise TypeError(f'Invalid type to insert: {type(item)}')
        super().insert(index, str(item))

    def append(self, item: DescriptionValue):
        if not isinstance(item, DescriptionValue):
            raise TypeError(f'Invalid type to append: {type(item)}')
        super().append(item)

    def extend(self, other: 'Description'):
        if not isinstance(other, type(self)):
            raise TypeError(f'Invalid type to extend: {type(other)}')
        super().extend(other)
