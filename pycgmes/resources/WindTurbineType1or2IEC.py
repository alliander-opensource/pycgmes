"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .WindTurbineType1or2Dynamics import WindTurbineType1or2Dynamics


@dataclass
class WindTurbineType1or2IEC(WindTurbineType1or2Dynamics):
    """
    Parent class supporting relationships to IEC wind turbines type 1 and type 2 including their control models.
      Generator model for wind turbine of IEC type 1 or type 2 is a standard asynchronous generator model.
      Reference: IEC 61400-27-1:2015, 5.5.2 and 5.5.3.

    WindMechIEC: Wind mechanical model associated with this wind generator type 1 or type 2 model.
    WindProtectionIEC: Wind turbune protection model associated with this wind generator type 1 or type 2 model.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    WindMechIEC: Optional[str] = None  # Type M:1 in CIM
    WindProtectionIEC: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindTurbineType1or2IEC\n"
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
            "WindMechIEC": [
                self.profiles.DY.value,
            ],
            "WindProtectionIEC": [
                self.profiles.DY.value,
            ],
        }
