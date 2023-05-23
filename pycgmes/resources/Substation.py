"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .EquipmentContainer import EquipmentContainer


@dataclass
class Substation(EquipmentContainer):
    """
    A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk
      is passed for the purposes of switching or modifying its characteristics.

    Region: The SubGeographicalRegion containing the substation.
    VoltageLevels: The voltage levels within this substation.
    DCConverterUnit: The DC converter unit belonging of the substation.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    Region: Optional[str] = None  # Type M:1 in CIM
    # *Association not used*
    # VoltageLevels : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # DCConverterUnit : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=Substation\n"
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
            "Region": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            "VoltageLevels": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            "DCConverterUnit": [
                self.profiles.EQ.value,
            ],
        }
