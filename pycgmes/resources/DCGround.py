"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .DCConductingEquipment import DCConductingEquipment


@dataclass(config=DataclassConfig)
class DCGround(DCConductingEquipment):
    """
    A ground within a DC system.

    inductance: Inductance to ground.
    r: Resistance to ground.
    """

    inductance: float = 0.0  # Type #Inductance in CIM
    r: float = 0.0  # Type #Resistance in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=DCGround"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.EQ.value,
            ],
            # Attributes
            "inductance": [
                Profile.EQ.value,
            ],
            "r": [
                Profile.EQ.value,
            ],
        }
