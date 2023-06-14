"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .DCConductingEquipment import DCConductingEquipment


@dataclass(config=DataclassConfig)
class DCLineSegment(DCConductingEquipment):
    """
    A wire or combination of wires not insulated from one another, with consistent electrical characteristics, used to
      carry direct current between points in the DC region of the power system.

    capacitance: Capacitance of the DC line segment. Significant for cables only.
    inductance: Inductance of the DC line segment. Negligible compared with DCSeriesDevice used for smoothing.
    resistance: Resistance of the DC line segment.
    length: Segment length for calculating line section capabilities.
    """

    capacitance: float = 0.0  # Type #Capacitance in CIM
    inductance: float = 0.0  # Type #Inductance in CIM
    resistance: float = 0.0  # Type #Resistance in CIM
    length: float = 0.0  # Type #Length in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=DCLineSegment"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "inductance": [
                Profile.EQ.value,
            ],
            "resistance": [
                Profile.EQ.value,
            ],
            "length": [
                Profile.EQ.value,
            ],
        }
