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
class ThermalGeneratingUnit(GeneratingUnit):
    """
    A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.

    CAESPlant: A thermal generating unit may be a member of a compressed air energy storage plant.
    CogenerationPlant: A thermal generating unit may be a member of a cogeneration plant.
    CombinedCyclePlant: A thermal generating unit may be a member of a combined cycle plant.
    FossilFuels: A thermal generating unit may have one or more fossil fuels.
    """

    CAESPlant: Optional[str] = None  # Type M:0..1 in CIM
    CogenerationPlant: Optional[str] = None  # Type M:0..1 in CIM
    CombinedCyclePlant: Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # FossilFuels : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ThermalGeneratingUnit"]
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
            "CAESPlant": [
                Profile.EQ.value,
            ],
            "CogenerationPlant": [
                Profile.EQ.value,
            ],
            "CombinedCyclePlant": [
                Profile.EQ.value,
            ],
            "FossilFuels": [
                Profile.EQ.value,
            ],
        }
