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
class HydroGeneratingUnit(GeneratingUnit):
    """
    A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan).

    energyConversionCapability: Energy conversion capability for generating.
    dropHeight: The height water drops from the reservoir mid-point to the turbine.
    turbineType: Type of turbine.
    HydroPowerPlant: The hydro generating unit belongs to a hydro power plant.
    """

    energyConversionCapability: Optional[str] = None  # Type M:0..1 in CIM
    dropHeight: float = 0.0  # Type #Length in CIM
    turbineType: Optional[str] = None  # Type M:0..1 in CIM
    HydroPowerPlant: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=HydroGeneratingUnit"]
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
            "energyConversionCapability": [
                Profile.EQ.value,
            ],
            "dropHeight": [
                Profile.EQ.value,
            ],
            "turbineType": [
                Profile.EQ.value,
            ],
            "HydroPowerPlant": [
                Profile.EQ.value,
            ],
        }
