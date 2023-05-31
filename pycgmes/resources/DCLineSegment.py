"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .DCConductingEquipment import DCConductingEquipment


@dataclass
class DCLineSegment(DCConductingEquipment):
    """
    A wire or combination of wires not insulated from one another, with consistent electrical characteristics, used to
      carry direct current between points in the DC region of the power system.

    capacitance: Capacitance of the DC line segment. Significant for cables only.
    inductance: Inductance of the DC line segment. Negligible compared with DCSeriesDevice used for smoothing.
    resistance: Resistance of the DC line segment.
    length: Segment length for calculating line section capabilities.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    capacitance: float = 0.0  # Type #Capacitance in CIM
    inductance: float = 0.0  # Type #Inductance in CIM
    resistance: float = 0.0  # Type #Resistance in CIM
    length: float = 0.0  # Type #Length in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=DCLineSegment\n"
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
                self.profiles.EQ.value,
            ],
            # Attributes
            "capacitance": [
                self.profiles.EQ.value,
            ],
            "inductance": [
                self.profiles.EQ.value,
            ],
            "resistance": [
                self.profiles.EQ.value,
            ],
            "length": [
                self.profiles.EQ.value,
            ],
        }
