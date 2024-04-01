from abc import ABC

from context.shared.domain.types.var_char_set_type import VarCharSetType
from context.shared.domain.types.var_char_type import VarCharType


class SubtagField(VarCharSetType, ABC):
    """The field 'Subtag' contains the subtag defined in the record.

    For more information: https://www.rfc-editor.org/rfc/bcp/bcp47.txt

    Examples:

     - "en"
     - "aao"
     - "Latn"
     - "GB"
     - "basiceng"""
