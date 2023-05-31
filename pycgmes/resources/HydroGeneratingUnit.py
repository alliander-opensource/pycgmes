"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .GeneratingUnit import GeneratingUnit


@dataclass
class HydroGeneratingUnit(GeneratingUnit):
    """
    A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan).

    energyConversionCapability: Energy conversion capability for generating.
    dropHeight: The height water drops from the reservoir mid-point to the turbine.
    turbineType: Type of turbine.
    HydroPowerPlant: The hydro generating unit belongs to a hydro power plant.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    energyConversionCapability: Optional[str] = None  # Type M:0..1 in CIM
    dropHeight: float = 0.0  # Type #Length in CIM
    turbineType: Optional[str] = None  # Type M:0..1 in CIM
    HydroPowerPlant: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=HydroGeneratingUnit\n"
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
            "energyConversionCapability": [
                self.profiles.EQ.value,
            ],
            "dropHeight": [
                self.profiles.EQ.value,
            ],
            "turbineType": [
                self.profiles.EQ.value,
            ],
            "HydroPowerPlant": [
                self.profiles.EQ.value,
            ],
        }
