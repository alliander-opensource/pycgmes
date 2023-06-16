"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindContPitchAngleIEC(IdentifiedObject):
    """
    Pitch angle control model. Reference: IEC 61400-27-1:2015, 5.6.5.2.

    dthetamax: Maximum pitch positive ramp rate (dthetamax) (> WindContPitchAngleIEC.dthetamin). It is a type-dependent
      parameter. Unit = degrees / s.
    dthetamin: Maximum pitch negative ramp rate (dthetamin) (< WindContPitchAngleIEC.dthetamax). It is a type-dependent
      parameter. Unit = degrees / s.
    kic: Power PI controller integration gain (KIc). It is a type-dependent parameter.
    kiomega: Speed PI controller integration gain (KIomega). It is a type-dependent parameter.
    kpc: Power PI controller proportional gain (KPc). It is a type-dependent parameter.
    kpomega: Speed PI controller proportional gain (KPomega). It is a type-dependent parameter.
    kpx: Pitch cross coupling gain (KPX). It is a type-dependent parameter.
    thetamax: Maximum pitch angle (thetamax) (> WindContPitchAngleIEC.thetamin). It is a type-dependent parameter.
    thetamin: Minimum pitch angle (thetamin) (< WindContPitchAngleIEC.thetamax). It is a type-dependent parameter.
    ttheta: Pitch time constant (ttheta) (>= 0). It is a type-dependent parameter.
    WindTurbineType3IEC: Wind turbine type 3 model with which this pitch control model is associated.
    """

    dthetamax: float = 0.0  # Type #Float in CIM
    dthetamin: float = 0.0  # Type #Float in CIM
    kic: float = 0.0  # Type #PU in CIM
    kiomega: float = 0.0  # Type #PU in CIM
    kpc: float = 0.0  # Type #PU in CIM
    kpomega: float = 0.0  # Type #PU in CIM
    kpx: float = 0.0  # Type #PU in CIM
    thetamax: float = 0.0  # Type #AngleDegrees in CIM
    thetamin: float = 0.0  # Type #AngleDegrees in CIM
    ttheta: int = 0  # Type #Seconds in CIM
    # *Association not used*
    # WindTurbineType3IEC : Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=WindContPitchAngleIEC"]
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
            "dthetamax": [
                Profile.DY.value,
            ],
            "dthetamin": [
                Profile.DY.value,
            ],
            "kic": [
                Profile.DY.value,
            ],
            "kiomega": [
                Profile.DY.value,
            ],
            "kpc": [
                Profile.DY.value,
            ],
            "kpomega": [
                Profile.DY.value,
            ],
            "kpx": [
                Profile.DY.value,
            ],
            "thetamax": [
                Profile.DY.value,
            ],
            "thetamin": [
                Profile.DY.value,
            ],
            "ttheta": [
                Profile.DY.value,
            ],
            "WindTurbineType3IEC": [
                Profile.DY.value,
            ],
        }
