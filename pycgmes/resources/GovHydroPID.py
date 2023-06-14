"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovHydroPID(TurbineGovernorDynamics):
    """
    PID governor and turbine.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    pmax: Maximum gate opening, PU of MWbase (Pmax) (> GovHydroPID.pmin).  Typical value = 1.
    pmin: Minimum gate opening, PU of MWbase (Pmin) (< GovHydroPID.pmax).  Typical value = 0.
    r: Steady state droop (R).  Typical value = 0,05.
    td: Input filter time constant (Td) (>= 0).  If = 0, block is bypassed.  Typical value = 0.
    tf: Washout time constant (Tf) (>= 0).  Typical value = 0,1.
    tp: Gate servo time constant (Tp) (>= 0).  If = 0, block is bypassed.  Typical value = 0,35.
    velop: Maximum gate opening velocity (Velop).  Unit = PU / s.  Typical value = 0,09.
    velcl: Maximum gate closing velocity (Velcl).  Unit = PU / s.  Typical value = -0,14.
    kd: Derivative gain (Kd).  Typical value = 1,11.
    kp: Proportional gain (Kp).  Typical value = 0,1.
    ki: Integral gain (Ki).  Typical value = 0,36.
    kg: Gate servo gain (Kg).  Typical value = 2,5.
    tturb: Turbine time constant (Tturb) (>= 0). See Parameter detail 3.  Typical value = 0,8.
    aturb: Turbine numerator multiplier (Aturb) (see parameter detail 3).  Typical value -1.
    bturb: Turbine denominator multiplier (Bturb) (see parameter detail 3).  Typical value = 0,5.
    tt: Power feedback time constant (Tt) (>= 0).  If = 0, block is bypassed.  Typical value = 0,02.
    db1: Intentional dead-band width (db1).  Unit = Hz.  Typical value = 0.
    inputSignal: Input signal switch (Flag).  true = Pe input is used false = feedback is received from CV. Flag is
      normally dependent on Tt.  If Tt is zero, Flag is set to false. If Tt is not zero, Flag is set to
      true.   Typical value = true.
    eps: Intentional db hysteresis (eps).  Unit = Hz.  Typical value = 0.
    db2: Unintentional dead-band (db2).  Unit = MW.  Typical value = 0.
    gv1: Nonlinear gain point 1, PU gv (Gv1).  Typical value = 0.
    pgv1: Nonlinear gain point 1, PU power (Pgv1).  Typical value = 0.
    gv2: Nonlinear gain point 2, PU gv (Gv2).  Typical value = 0.
    pgv2: Nonlinear gain point 2, PU power (Pgv2).  Typical value = 0.
    gv3: Nonlinear gain point 3, PU gv (Gv3).  Typical value = 0.
    pgv3: Nonlinear gain point 3, PU power (Pgv3).  Typical value = 0.
    gv4: Nonlinear gain point 4, PU gv (Gv4).  Typical value = 0.
    pgv4: Nonlinear gain point 4, PU power (Pgv4).  Typical value = 0.
    gv5: Nonlinear gain point 5, PU gv (Gv5).  Typical value = 0.
    pgv5: Nonlinear gain point 5, PU power (Pgv5).  Typical value = 0.
    gv6: Nonlinear gain point 6, PU gv (Gv6).  Typical value = 0.
    pgv6: Nonlinear gain point 6, PU power (Pgv6).  Typical value = 0.
    """

    mwbase: float = 0.0  # Type #ActivePower in CIM
    pmax: float = 0.0  # Type #PU in CIM
    pmin: float = 0.0  # Type #PU in CIM
    r: float = 0.0  # Type #PU in CIM
    td: int = 0  # Type #Seconds in CIM
    tf: int = 0  # Type #Seconds in CIM
    tp: int = 0  # Type #Seconds in CIM
    velop: float = 0.0  # Type #Float in CIM
    velcl: float = 0.0  # Type #Float in CIM
    kd: float = 0.0  # Type #PU in CIM
    kp: float = 0.0  # Type #PU in CIM
    ki: float = 0.0  # Type #PU in CIM
    kg: float = 0.0  # Type #PU in CIM
    tturb: int = 0  # Type #Seconds in CIM
    aturb: float = 0.0  # Type #PU in CIM
    bturb: float = 0.0  # Type #PU in CIM
    tt: int = 0  # Type #Seconds in CIM
    db1: float = 0.0  # Type #Frequency in CIM
    inputSignal: bool = False  # Type #Boolean in CIM
    eps: float = 0.0  # Type #Frequency in CIM
    db2: float = 0.0  # Type #ActivePower in CIM
    gv1: float = 0.0  # Type #PU in CIM
    pgv1: float = 0.0  # Type #PU in CIM
    gv2: float = 0.0  # Type #PU in CIM
    pgv2: float = 0.0  # Type #PU in CIM
    gv3: float = 0.0  # Type #PU in CIM
    pgv3: float = 0.0  # Type #PU in CIM
    gv4: float = 0.0  # Type #PU in CIM
    pgv4: float = 0.0  # Type #PU in CIM
    gv5: float = 0.0  # Type #PU in CIM
    pgv5: float = 0.0  # Type #PU in CIM
    gv6: float = 0.0  # Type #PU in CIM
    pgv6: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=GovHydroPID"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "mwbase": [
                Profile.DY.value,
            ],
            "pmax": [
                Profile.DY.value,
            ],
            "pmin": [
                Profile.DY.value,
            ],
            "r": [
                Profile.DY.value,
            ],
            "td": [
                Profile.DY.value,
            ],
            "tf": [
                Profile.DY.value,
            ],
            "tp": [
                Profile.DY.value,
            ],
            "velop": [
                Profile.DY.value,
            ],
            "velcl": [
                Profile.DY.value,
            ],
            "kd": [
                Profile.DY.value,
            ],
            "kp": [
                Profile.DY.value,
            ],
            "ki": [
                Profile.DY.value,
            ],
            "kg": [
                Profile.DY.value,
            ],
            "tturb": [
                Profile.DY.value,
            ],
            "aturb": [
                Profile.DY.value,
            ],
            "bturb": [
                Profile.DY.value,
            ],
            "tt": [
                Profile.DY.value,
            ],
            "db1": [
                Profile.DY.value,
            ],
            "inputSignal": [
                Profile.DY.value,
            ],
            "eps": [
                Profile.DY.value,
            ],
            "db2": [
                Profile.DY.value,
            ],
            "gv1": [
                Profile.DY.value,
            ],
            "pgv1": [
                Profile.DY.value,
            ],
            "gv2": [
                Profile.DY.value,
            ],
            "pgv2": [
                Profile.DY.value,
            ],
            "gv3": [
                Profile.DY.value,
            ],
            "pgv3": [
                Profile.DY.value,
            ],
            "gv4": [
                Profile.DY.value,
            ],
            "pgv4": [
                Profile.DY.value,
            ],
            "gv5": [
                Profile.DY.value,
            ],
            "pgv5": [
                Profile.DY.value,
            ],
            "gv6": [
                Profile.DY.value,
            ],
            "pgv6": [
                Profile.DY.value,
            ],
        }
