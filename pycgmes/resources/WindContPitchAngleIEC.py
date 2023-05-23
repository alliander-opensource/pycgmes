"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=WindContPitchAngleIEC\n"
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
            "dthetamax": [
                self.profiles.DY.value,
            ],
            "dthetamin": [
                self.profiles.DY.value,
            ],
            "kic": [
                self.profiles.DY.value,
            ],
            "kiomega": [
                self.profiles.DY.value,
            ],
            "kpc": [
                self.profiles.DY.value,
            ],
            "kpomega": [
                self.profiles.DY.value,
            ],
            "kpx": [
                self.profiles.DY.value,
            ],
            "thetamax": [
                self.profiles.DY.value,
            ],
            "thetamin": [
                self.profiles.DY.value,
            ],
            "ttheta": [
                self.profiles.DY.value,
            ],
            "WindTurbineType3IEC": [
                self.profiles.DY.value,
            ],
        }
