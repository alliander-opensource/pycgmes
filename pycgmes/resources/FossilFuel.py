"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
class FossilFuel(IdentifiedObject):
    """
    The fossil fuel consumed by the non-nuclear thermal generating unit.   For example, coal, oil, gas, etc.   These are
      the specific fuels that the generating unit can consume.

    fossilFuelType: The type of fossil fuel, such as coal, oil, or gas.
    ThermalGeneratingUnit: A thermal generating unit may have one or more fossil fuels.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    fossilFuelType: Optional[str] = None  # Type M:1..1 in CIM
    ThermalGeneratingUnit: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=FossilFuel\n"
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
            "fossilFuelType": [
                self.profiles.EQ.value,
            ],
            "ThermalGeneratingUnit": [
                self.profiles.EQ.value,
            ],
        }
