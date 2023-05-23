"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .WindTurbineType4IEC import WindTurbineType4IEC


@dataclass
class WindTurbineType4aIEC(WindTurbineType4IEC):
    """
    Wind turbine IEC type 4A. Reference: IEC 61400-27-1:2015, 5.5.5.2.

    WindContPType4aIEC: Wind control P type 4A model associated with this wind turbine type 4A model.
    WindGenType4IEC: Wind generator type 4 model associated with this wind turbine type 4A model.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    WindContPType4aIEC: Optional[str] = None  # Type M:1 in CIM
    WindGenType4IEC: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindTurbineType4aIEC\n"
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
            "WindContPType4aIEC": [
                self.profiles.DY.value,
            ],
            "WindGenType4IEC": [
                self.profiles.DY.value,
            ],
        }
