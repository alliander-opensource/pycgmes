"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .WindTurbineType3or4IEC import WindTurbineType3or4IEC


@dataclass
class WindTurbineType4IEC(WindTurbineType3or4IEC):
    """
    Parent class supporting relationships to IEC wind turbines type 4 including their control models.

    WindGenType3aIEC: Wind generator type 3A model associated with this wind turbine type 4 model.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    WindGenType3aIEC: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindTurbineType4IEC\n"
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
                self.profiles.DY.value,
            ],
            # Attributes
            "WindGenType3aIEC": [
                self.profiles.DY.value,
            ],
        }
