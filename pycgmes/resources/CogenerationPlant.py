"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .PowerSystemResource import PowerSystemResource


@dataclass
class CogenerationPlant(PowerSystemResource):
    """
    A set of thermal generating units for the production of electrical energy and process steam (usually from the output
      of the steam turbines). The steam sendout is typically used for industrial purposes or for municipal heating
      and cooling.

    ThermalGeneratingUnits: A thermal generating unit may be a member of a cogeneration plant.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # ThermalGeneratingUnits : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=CogenerationPlant\n"
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
            "ThermalGeneratingUnits": [
                self.profiles.EQ.value,
            ],
        }
