"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
class ValueToAlias(IdentifiedObject):
    """
    Describes the translation of one particular value into a name, e.g. 1 as "Open".

    ValueAliasSet: The ValueAliasSet having the ValueToAlias mappings.
    value: The value that is mapped.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ValueAliasSet: Optional[str] = None  # Type M:1 in CIM
    value: int = 0  # Type #Integer in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ValueToAlias\n"
        attributes = self.__dict__
        for key, val in attributes.items():
            str_ = str_ + key + f"={val}\n"
        return str_

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                self.profiles.OP.value,
            ],
            # Attributes
            "ValueAliasSet": [
                self.profiles.OP.value,
            ],
            "value": [
                self.profiles.OP.value,
            ],
        }
