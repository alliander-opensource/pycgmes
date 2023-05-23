"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .GeneratingUnit import GeneratingUnit


@dataclass
class SolarGeneratingUnit(GeneratingUnit):
    """
    A solar thermal generating unit, connected to the grid by means of a rotating machine.  This class does not
      represent photovoltaic (PV) generation.

    SolarPowerPlant: A solar power plant may have solar generating units.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    SolarPowerPlant: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=SolarGeneratingUnit\n"
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
                self.profiles.SSH.value,
            ],
            # Attributes
            "SolarPowerPlant": [
                self.profiles.EQ.value,
            ],
        }
