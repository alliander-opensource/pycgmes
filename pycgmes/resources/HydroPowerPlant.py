"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .PowerSystemResource import PowerSystemResource


@dataclass
class HydroPowerPlant(PowerSystemResource):
    """
    A hydro power station which can generate or pump. When generating, the generator turbines receive water from an
      upper reservoir. When pumping, the pumps receive their water from a lower reservoir.

    HydroGeneratingUnits: The hydro generating unit belongs to a hydro power plant.
    hydroPlantStorageType: The type of hydro power plant water storage.
    HydroPumps: The hydro pump may be a member of a pumped storage plant or a pump for distributing water.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # HydroGeneratingUnits : list = field(default_factory=list)  # Type M:0..n in CIM
    hydroPlantStorageType: Optional[str] = None  # Type M:1..1 in CIM
    # *Association not used*
    # HydroPumps : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=HydroPowerPlant\n"
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
            "HydroGeneratingUnits": [
                self.profiles.EQ.value,
            ],
            "hydroPlantStorageType": [
                self.profiles.EQ.value,
            ],
            "HydroPumps": [
                self.profiles.EQ.value,
            ],
        }
