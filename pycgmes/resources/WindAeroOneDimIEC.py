"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindAeroOneDimIEC(IdentifiedObject):
    """
    One-dimensional aerodynamic model.   Reference: IEC 61400-27-1:2015, 5.6.1.2.

    ka: Aerodynamic gain (ka). It is a type-dependent parameter.
    thetaomega: Initial pitch angle (thetaomega0). It is a case-dependent parameter.
    WindTurbineType3IEC: Wind turbine type 3 model with which this wind aerodynamic model is associated.
    """

    ka: float = 0.0  # Type #Float in CIM
    thetaomega: float = 0.0  # Type #AngleDegrees in CIM
    # *Association not used*
    # WindTurbineType3IEC : Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=WindAeroOneDimIEC"]
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
            "ka": [
                Profile.DY.value,
            ],
            "thetaomega": [
                Profile.DY.value,
            ],
            "WindTurbineType3IEC": [
                Profile.DY.value,
            ],
        }
