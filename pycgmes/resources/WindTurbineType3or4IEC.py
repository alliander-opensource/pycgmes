"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .WindTurbineType3or4Dynamics import WindTurbineType3or4Dynamics


@dataclass
class WindTurbineType3or4IEC(WindTurbineType3or4Dynamics):
    """
    Parent class supporting relationships to IEC wind turbines type 3 and type 4 including their control models.

    WindContCurrLimIEC: Wind control current limitation model associated with this wind turbine type 3 or type 4 model.
    WIndContQIEC: Wind control Q model associated with this wind turbine type 3 or type 4 model.
    WindContQLimIEC: Constant Q limitation model associated with this wind generator type 3 or type 4 model.
    WindContQPQULimIEC: QP and QU limitation model associated with this wind generator type 3 or type 4 model.
    WindProtectionIEC: Wind turbune protection model associated with this wind generator type 3 or type 4 model.
    WindRefFrameRotIEC: Reference frame rotation model associated with this wind turbine type 3 or type 4 model.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    WindContCurrLimIEC: Optional[str] = None  # Type M:1 in CIM
    WIndContQIEC: Optional[str] = None  # Type M:1 in CIM
    WindContQLimIEC: Optional[str] = None  # Type M:0..1 in CIM
    WindContQPQULimIEC: Optional[str] = None  # Type M:0..1 in CIM
    WindProtectionIEC: Optional[str] = None  # Type M:1 in CIM
    WindRefFrameRotIEC: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindTurbineType3or4IEC\n"
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
            "WindContCurrLimIEC": [
                self.profiles.DY.value,
            ],
            "WIndContQIEC": [
                self.profiles.DY.value,
            ],
            "WindContQLimIEC": [
                self.profiles.DY.value,
            ],
            "WindContQPQULimIEC": [
                self.profiles.DY.value,
            ],
            "WindProtectionIEC": [
                self.profiles.DY.value,
            ],
            "WindRefFrameRotIEC": [
                self.profiles.DY.value,
            ],
        }
