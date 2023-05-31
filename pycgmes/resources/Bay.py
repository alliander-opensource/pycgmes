"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .EquipmentContainer import EquipmentContainer


@dataclass
class Bay(EquipmentContainer):
    """
    A collection of power system resources (within a given substation) including conducting equipment, protection
      relays, measurements, and telemetry.  A bay typically represents a physical grouping related to modularization
      of equipment.

    VoltageLevel: The voltage level containing this bay.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    VoltageLevel: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=Bay\n"
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
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            # Attributes
            "VoltageLevel": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
        }
