"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .GeneratingUnit import GeneratingUnit


@dataclass
class WindGeneratingUnit(GeneratingUnit):
    """
    A wind driven generating unit, connected to the grid by means of a rotating machine.  May be used to represent a
      single turbine or an aggregation.

    windGenUnitType: The kind of wind generating unit.
    WindPowerPlant: A wind power plant may have wind generating units.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    windGenUnitType: Optional[str] = None  # Type M:1..1 in CIM
    WindPowerPlant: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindGeneratingUnit\n"
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
            "windGenUnitType": [
                self.profiles.EQ.value,
            ],
            "WindPowerPlant": [
                self.profiles.EQ.value,
            ],
        }
