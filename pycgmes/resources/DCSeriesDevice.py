"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .DCConductingEquipment import DCConductingEquipment


@dataclass(config=DataclassConfig)
class DCSeriesDevice(DCConductingEquipment):
    """
    A series device within the DC system, typically a reactor used for filtering or smoothing.  Needed for transient and
      short circuit studies.

    inductance: Inductance of the device.
    resistance: Resistance of the DC device.
    """

    inductance: float = 0.0  # Type #Inductance in CIM
    resistance: float = 0.0  # Type #Resistance in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=DCSeriesDevice"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "resistance": [
                Profile.EQ.value,
            ],
        }
