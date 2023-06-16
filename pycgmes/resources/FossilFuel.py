"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class FossilFuel(IdentifiedObject):
    """
    The fossil fuel consumed by the non-nuclear thermal generating unit.   For example, coal, oil, gas, etc.   These are
      the specific fuels that the generating unit can consume.

    fossilFuelType: The type of fossil fuel, such as coal, oil, or gas.
    ThermalGeneratingUnit: A thermal generating unit may have one or more fossil fuels.
    """

    fossilFuelType: Optional[str] = None  # Type M:1..1 in CIM
    ThermalGeneratingUnit: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=FossilFuel"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "fossilFuelType": [
                Profile.EQ.value,
            ],
            "ThermalGeneratingUnit": [
                Profile.EQ.value,
            ],
        }
