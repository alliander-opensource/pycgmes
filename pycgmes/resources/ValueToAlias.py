"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class ValueToAlias(IdentifiedObject):
    """
    Describes the translation of one particular value into a name, e.g. 1 as "Open".

    ValueAliasSet: The ValueAliasSet having the ValueToAlias mappings.
    value: The value that is mapped.
    """

    ValueAliasSet: Optional[str] = None  # Type M:1 in CIM
    value: int = 0  # Type #Integer in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ValueToAlias"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
        )

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                Profile.OP.value,
            ],
            # Attributes
            "ValueAliasSet": [
                Profile.OP.value,
            ],
            "value": [
                Profile.OP.value,
            ],
        }
