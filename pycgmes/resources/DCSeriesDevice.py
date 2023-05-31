"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .DCConductingEquipment import DCConductingEquipment


@dataclass
class DCSeriesDevice(DCConductingEquipment):
    """
    A series device within the DC system, typically a reactor used for filtering or smoothing.  Needed for transient and
      short circuit studies.

    inductance: Inductance of the device.
    resistance: Resistance of the DC device.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    inductance: float = 0.0  # Type #Inductance in CIM
    resistance: float = 0.0  # Type #Resistance in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=DCSeriesDevice\n"
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
            "inductance": [
                self.profiles.EQ.value,
            ],
            "resistance": [
                self.profiles.EQ.value,
            ],
        }
