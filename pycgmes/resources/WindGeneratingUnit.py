"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .GeneratingUnit import GeneratingUnit


@dataclass(config=DataclassConfig)
class WindGeneratingUnit(GeneratingUnit):
    """
    A wind driven generating unit, connected to the grid by means of a rotating machine.  May be used to represent a
      single turbine or an aggregation.

    windGenUnitType: The kind of wind generating unit.
    WindPowerPlant: A wind power plant may have wind generating units.
    """

    windGenUnitType: Optional[str] = None  # Type M:1..1 in CIM
    WindPowerPlant: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=WindGeneratingUnit"]
            + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.SSH.value,
            ],
            # Attributes
            "windGenUnitType": [
                Profile.EQ.value,
            ],
            "WindPowerPlant": [
                Profile.EQ.value,
            ],
        }
