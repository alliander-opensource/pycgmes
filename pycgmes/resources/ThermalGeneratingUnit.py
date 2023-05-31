"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .GeneratingUnit import GeneratingUnit


@dataclass
class ThermalGeneratingUnit(GeneratingUnit):
    """
    A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.

    CAESPlant: A thermal generating unit may be a member of a compressed air energy storage plant.
    CogenerationPlant: A thermal generating unit may be a member of a cogeneration plant.
    CombinedCyclePlant: A thermal generating unit may be a member of a combined cycle plant.
    FossilFuels: A thermal generating unit may have one or more fossil fuels.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    CAESPlant: Optional[str] = None  # Type M:0..1 in CIM
    CogenerationPlant: Optional[str] = None  # Type M:0..1 in CIM
    CombinedCyclePlant: Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # FossilFuels : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ThermalGeneratingUnit\n"
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
            "CAESPlant": [
                self.profiles.EQ.value,
            ],
            "CogenerationPlant": [
                self.profiles.EQ.value,
            ],
            "CombinedCyclePlant": [
                self.profiles.EQ.value,
            ],
            "FossilFuels": [
                self.profiles.EQ.value,
            ],
        }
