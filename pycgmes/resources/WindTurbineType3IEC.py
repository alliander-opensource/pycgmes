"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .WindTurbineType3or4IEC import WindTurbineType3or4IEC


@dataclass
class WindTurbineType3IEC(WindTurbineType3or4IEC):
    """
    Parent class supporting relationships to IEC wind turbines type 3 including their control models.

    WindAeroOneDimIEC: Wind aerodynamic model associated with this wind generator type 3 model.
    WindAeroTwoDimIEC: Wind aerodynamic model associated with this wind turbine type 3 model.
    WindContPitchAngleIEC: Wind control pitch angle model associated with this wind turbine type 3.
    WindContPType3IEC: Wind control P type 3 model associated with this wind turbine type 3 model.
    WindGenType3IEC: Wind generator type 3 model associated with this wind turbine type 3 model.
    WindMechIEC: Wind mechanical model associated with this wind turbine type 3 model.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    WindAeroOneDimIEC: Optional[str] = None  # Type M:0..1 in CIM
    WindAeroTwoDimIEC: Optional[str] = None  # Type M:0..1 in CIM
    WindContPitchAngleIEC: Optional[str] = None  # Type M:1 in CIM
    WindContPType3IEC: Optional[str] = None  # Type M:1 in CIM
    WindGenType3IEC: Optional[str] = None  # Type M:0..1 in CIM
    WindMechIEC: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindTurbineType3IEC\n"
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
            "WindAeroOneDimIEC": [
                self.profiles.DY.value,
            ],
            "WindAeroTwoDimIEC": [
                self.profiles.DY.value,
            ],
            "WindContPitchAngleIEC": [
                self.profiles.DY.value,
            ],
            "WindContPType3IEC": [
                self.profiles.DY.value,
            ],
            "WindGenType3IEC": [
                self.profiles.DY.value,
            ],
            "WindMechIEC": [
                self.profiles.DY.value,
            ],
        }
