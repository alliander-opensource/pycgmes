"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .WindTurbineType3or4IEC import WindTurbineType3or4IEC


@dataclass(config=DataclassConfig)
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

    WindAeroOneDimIEC: Optional[str] = None  # Type M:0..1 in CIM
    WindAeroTwoDimIEC: Optional[str] = None  # Type M:0..1 in CIM
    WindContPitchAngleIEC: Optional[str] = None  # Type M:1 in CIM
    WindContPType3IEC: Optional[str] = None  # Type M:1 in CIM
    WindGenType3IEC: Optional[str] = None  # Type M:0..1 in CIM
    WindMechIEC: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=WindTurbineType3IEC"]
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
                Profile.DY.value,
            ],
            # Attributes
            "WindAeroOneDimIEC": [
                Profile.DY.value,
            ],
            "WindAeroTwoDimIEC": [
                Profile.DY.value,
            ],
            "WindContPitchAngleIEC": [
                Profile.DY.value,
            ],
            "WindContPType3IEC": [
                Profile.DY.value,
            ],
            "WindGenType3IEC": [
                Profile.DY.value,
            ],
            "WindMechIEC": [
                Profile.DY.value,
            ],
        }
