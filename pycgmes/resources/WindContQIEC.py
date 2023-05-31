"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
class WindContQIEC(IdentifiedObject):
    """
    Q control model. Reference: IEC 61400-27-1:2015, 5.6.5.7.

    iqh1: Maximum reactive current injection during dip (iqh1). It is a type-dependent parameter.
    iqmax: Maximum reactive current injection (iqmax) (> WindContQIEC.iqmin). It is a type-dependent parameter.
    iqmin: Minimum reactive current injection (iqmin) (< WindContQIEC.iqmax). It is a type-dependent parameter.
    iqpost: Post fault reactive current injection (iqpost). It is a project-dependent parameter.
    kiq: Reactive power PI controller integration gain (KI,q). It is a type-dependent parameter.
    kiu: Voltage PI controller integration gain (KI,u). It is a type-dependent parameter.
    kpq: Reactive power PI controller proportional gain (KP,q). It is a type-dependent parameter.
    kpu: Voltage PI controller proportional gain (KP,u). It is a type-dependent parameter.
    kqv: Voltage scaling factor for UVRT current (Kqv). It is a project-dependent parameter.
    tpfiltq: Power measurement filter time constant (Tpfiltq) (>= 0). It is a type-dependent parameter.
    rdroop: Resistive component of voltage drop impedance (rdroop) (>= 0). It is a project-dependent parameter.
    tufiltq: Voltage measurement filter time constant (Tufiltq) (>= 0). It is a type-dependent parameter.
    tpost: Length of time period where post fault reactive power is injected (Tpost) (>= 0). It is a project-dependent
      parameter.
    tqord: Time constant in reactive power order lag (Tqord) (>= 0). It is a type-dependent parameter.
    udb1: Voltage deadband lower limit (udb1). It is a type-dependent parameter.
    udb2: Voltage deadband upper limit (udb2). It is a type-dependent parameter.
    umax: Maximum voltage in voltage PI controller integral term (umax) (> WindContQIEC.umin). It is a type-dependent
      parameter.
    umin: Minimum voltage in voltage PI controller integral term (umin) (< WindContQIEC.umax). It is a type-dependent
      parameter.
    uqdip: Voltage threshold for UVRT detection in Q control (uqdip). It is a type-dependent parameter.
    uref0: User-defined bias in voltage reference (uref0). It is a case-dependent parameter.
    windQcontrolModesType: Types of general wind turbine Q control modes (MqG).  It is a project-dependent parameter.
    windUVRTQcontrolModesType: Types of UVRT Q control modes (MqUVRT). It is a project-dependent parameter.
    xdroop: Inductive component of voltage drop impedance (xdroop) (>= 0). It is a project-dependent parameter.
    WindTurbineType3or4IEC: Wind turbine type 3 or type 4 model with which this reactive control model is associated.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    iqh1: float = 0.0  # Type #PU in CIM
    iqmax: float = 0.0  # Type #PU in CIM
    iqmin: float = 0.0  # Type #PU in CIM
    iqpost: float = 0.0  # Type #PU in CIM
    kiq: float = 0.0  # Type #PU in CIM
    kiu: float = 0.0  # Type #PU in CIM
    kpq: float = 0.0  # Type #PU in CIM
    kpu: float = 0.0  # Type #PU in CIM
    kqv: float = 0.0  # Type #PU in CIM
    tpfiltq: int = 0  # Type #Seconds in CIM
    rdroop: float = 0.0  # Type #PU in CIM
    tufiltq: int = 0  # Type #Seconds in CIM
    tpost: int = 0  # Type #Seconds in CIM
    tqord: int = 0  # Type #Seconds in CIM
    udb1: float = 0.0  # Type #PU in CIM
    udb2: float = 0.0  # Type #PU in CIM
    umax: float = 0.0  # Type #PU in CIM
    umin: float = 0.0  # Type #PU in CIM
    uqdip: float = 0.0  # Type #PU in CIM
    uref0: float = 0.0  # Type #PU in CIM
    windQcontrolModesType: Optional[str] = None  # Type M:1..1 in CIM
    windUVRTQcontrolModesType: Optional[str] = None  # Type M:1..1 in CIM
    xdroop: float = 0.0  # Type #PU in CIM
    # *Association not used*
    # WindTurbineType3or4IEC : Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=WindContQIEC\n"
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
            "iqh1": [
                self.profiles.DY.value,
            ],
            "iqmax": [
                self.profiles.DY.value,
            ],
            "iqmin": [
                self.profiles.DY.value,
            ],
            "iqpost": [
                self.profiles.DY.value,
            ],
            "kiq": [
                self.profiles.DY.value,
            ],
            "kiu": [
                self.profiles.DY.value,
            ],
            "kpq": [
                self.profiles.DY.value,
            ],
            "kpu": [
                self.profiles.DY.value,
            ],
            "kqv": [
                self.profiles.DY.value,
            ],
            "tpfiltq": [
                self.profiles.DY.value,
            ],
            "rdroop": [
                self.profiles.DY.value,
            ],
            "tufiltq": [
                self.profiles.DY.value,
            ],
            "tpost": [
                self.profiles.DY.value,
            ],
            "tqord": [
                self.profiles.DY.value,
            ],
            "udb1": [
                self.profiles.DY.value,
            ],
            "udb2": [
                self.profiles.DY.value,
            ],
            "umax": [
                self.profiles.DY.value,
            ],
            "umin": [
                self.profiles.DY.value,
            ],
            "uqdip": [
                self.profiles.DY.value,
            ],
            "uref0": [
                self.profiles.DY.value,
            ],
            "windQcontrolModesType": [
                self.profiles.DY.value,
            ],
            "windUVRTQcontrolModesType": [
                self.profiles.DY.value,
            ],
            "xdroop": [
                self.profiles.DY.value,
            ],
            "WindTurbineType3or4IEC": [
                self.profiles.DY.value,
            ],
        }
