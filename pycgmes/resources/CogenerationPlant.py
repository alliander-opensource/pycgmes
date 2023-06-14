"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PowerSystemResource import PowerSystemResource


@dataclass(config=DataclassConfig)
class CogenerationPlant(PowerSystemResource):
    """
    A set of thermal generating units for the production of electrical energy and process steam (usually from the output
      of the steam turbines). The steam sendout is typically used for industrial purposes or for municipal heating
      and cooling.

    ThermalGeneratingUnits: A thermal generating unit may be a member of a cogeneration plant.
    """

    # *Association not used*
    # ThermalGeneratingUnits : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=CogenerationPlant"]
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
            ],
            # Attributes
            "ThermalGeneratingUnits": [
                Profile.EQ.value,
            ],
        }
