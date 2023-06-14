"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .DCBaseTerminal import DCBaseTerminal


@dataclass(config=DataclassConfig)
class DCTerminal(DCBaseTerminal):
    """
    An electrical connection point to generic DC conducting equipment.

    DCConductingEquipment: An DC  terminal belong to a DC conducting equipment.
    """

    DCConductingEquipment: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=DCTerminal"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.TP.value,
                Profile.EQ.value,
                Profile.SSH.value,
            ],
            # Attributes
            "DCConductingEquipment": [
                Profile.EQ.value,
            ],
        }
