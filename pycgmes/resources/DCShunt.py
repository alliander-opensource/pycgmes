"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .DCConductingEquipment import DCConductingEquipment


@dataclass(config=DataclassConfig)
class DCShunt(DCConductingEquipment):
    """
    A shunt device within the DC system, typically used for filtering.  Needed for transient and short circuit studies.

    capacitance: Capacitance of the DC shunt.
    resistance: Resistance of the DC device.
    """

    capacitance: float = 0.0  # Type #Capacitance in CIM
    resistance: float = 0.0  # Type #Resistance in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=DCShunt"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "capacitance": [
                Profile.EQ.value,
            ],
            "resistance": [
                Profile.EQ.value,
            ],
        }
