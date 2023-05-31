"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Equipment import Equipment


@dataclass
class HydroPump(Equipment):
    """
    A synchronous motor-driven pump, typically associated with a pumped storage plant.

    HydroPowerPlant: The hydro pump may be a member of a pumped storage plant or a pump for distributing water.
    RotatingMachine: The synchronous machine drives the turbine which moves the water from a low elevation to a higher
      elevation. The direction of machine rotation for pumping may or may not be the same as for
      generating.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    HydroPowerPlant: Optional[str] = None  # Type M:0..1 in CIM
    RotatingMachine: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=HydroPump\n"
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
            "HydroPowerPlant": [
                self.profiles.EQ.value,
            ],
            "RotatingMachine": [
                self.profiles.EQ.value,
            ],
        }
