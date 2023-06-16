"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovSteam1(TurbineGovernorDynamics):
    """
    Steam turbine governor, based on the GovSteamIEEE1 (with optional deadband and nonlinear valve gain added).

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    k: Governor gain (reciprocal of droop) (K) (> 0).  Typical value = 25.
    t1: Governor lag time constant (T1) (>= 0).  Typical value = 0.
    t2: Governor lead time constant (T2) (>= 0).  Typical value = 0.
    t3: Valve positioner time constant (T3) (> 0).  Typical value = 0,1.
    uo: Maximum valve opening velocity (Uo) (> 0).  Unit = PU / s.  Typical value = 1.
    uc: Maximum valve closing velocity (Uc) (< 0).  Unit = PU / s.  Typical value = -10.
    pmax: Maximum valve opening (Pmax) (> GovSteam1.pmin).  Typical value = 1.
    pmin: Minimum valve opening (Pmin) (>= 0 and < GovSteam1.pmax).  Typical value = 0.
    t4: Inlet piping/steam bowl time constant (T4) (>= 0).  Typical value = 0,3.
    k1: Fraction of HP shaft power after first boiler pass (K1).  Typical value = 0,2.
    k2: Fraction of LP shaft power after first boiler pass (K2).  Typical value = 0.
    t5: Time constant of second boiler pass (T5) (>= 0).  Typical value = 5.
    k3: Fraction of HP shaft power after second boiler pass (K3).  Typical value = 0,3.
    k4: Fraction of LP shaft power after second boiler pass (K4).  Typical value = 0.
    t6: Time constant of third boiler pass (T6) (>= 0).  Typical value = 0,5.
    k5: Fraction of HP shaft power after third boiler pass (K5).  Typical value = 0,5.
    k6: Fraction of LP shaft power after third boiler pass (K6).  Typical value = 0.
    t7: Time constant of fourth boiler pass (T7) (>= 0).  Typical value = 0.
    k7: Fraction of HP shaft power after fourth boiler pass (K7).  Typical value = 0.
    k8: Fraction of LP shaft power after fourth boiler pass (K8).  Typical value = 0.
    db1: Intentional deadband width (db1).  Unit = Hz.  Typical value = 0.
    eps: Intentional db hysteresis (eps).  Unit = Hz.  Typical value = 0.
    sdb1: Intentional deadband indicator. true = intentional deadband is applied false = intentional deadband is not
      applied. Typical value = true.
    sdb2: Unintentional deadband location. true = intentional deadband is applied before point `A` false = intentional
      deadband is applied after point `A`. Typical value = true.
    db2: Unintentional deadband (db2).  Unit = MW.  Typical value = 0.
    valve: Nonlinear valve characteristic. true = nonlinear valve characteristic is used false = nonlinear valve
      characteristic is not used. Typical value = true.
    gv1: Nonlinear gain valve position point 1 (GV1).  Typical value = 0.
    pgv1: Nonlinear gain power value point 1 (Pgv1).  Typical value = 0.
    gv2: Nonlinear gain valve position point 2 (GV2).  Typical value = 0,4.
    pgv2: Nonlinear gain power value point 2 (Pgv2).  Typical value = 0,75.
    gv3: Nonlinear gain valve position point 3 (GV3).  Typical value = 0,5.
    pgv3: Nonlinear gain power value point 3 (Pgv3).  Typical value = 0,91.
    gv4: Nonlinear gain valve position point 4 (GV4).  Typical value = 0,6.
    pgv4: Nonlinear gain power value point 4 (Pgv4).  Typical value = 0,98.
    gv5: Nonlinear gain valve position point 5 (GV5).  Typical value = 1.
    pgv5: Nonlinear gain power value point 5 (Pgv5).  Typical value = 1.
    gv6: Nonlinear gain valve position point 6 (GV6).  Typical value = 0.
    pgv6: Nonlinear gain power value point 6 (Pgv6).  Typical value = 0.
    """

    mwbase: float = 0.0  # Type #ActivePower in CIM
    k: float = 0.0  # Type #PU in CIM
    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    uo: float = 0.0  # Type #Float in CIM
    uc: float = 0.0  # Type #Float in CIM
    pmax: float = 0.0  # Type #PU in CIM
    pmin: float = 0.0  # Type #PU in CIM
    t4: int = 0  # Type #Seconds in CIM
    k1: float = 0.0  # Type #Float in CIM
    k2: float = 0.0  # Type #Float in CIM
    t5: int = 0  # Type #Seconds in CIM
    k3: float = 0.0  # Type #Float in CIM
    k4: float = 0.0  # Type #Float in CIM
    t6: int = 0  # Type #Seconds in CIM
    k5: float = 0.0  # Type #Float in CIM
    k6: float = 0.0  # Type #Float in CIM
    t7: int = 0  # Type #Seconds in CIM
    k7: float = 0.0  # Type #Float in CIM
    k8: float = 0.0  # Type #Float in CIM
    db1: float = 0.0  # Type #Frequency in CIM
    eps: float = 0.0  # Type #Frequency in CIM
    sdb1: bool = False  # Type #Boolean in CIM
    sdb2: bool = False  # Type #Boolean in CIM
    db2: float = 0.0  # Type #ActivePower in CIM
    valve: bool = False  # Type #Boolean in CIM
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
            ["class=GovSteam1"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "k": [
                Profile.DY.value,
            ],
            "t1": [
                Profile.DY.value,
            ],
            "t2": [
                Profile.DY.value,
            ],
            "t3": [
                Profile.DY.value,
            ],
            "uo": [
                Profile.DY.value,
            ],
            "uc": [
                Profile.DY.value,
            ],
            "pmax": [
                Profile.DY.value,
            ],
            "pmin": [
                Profile.DY.value,
            ],
            "t4": [
                Profile.DY.value,
            ],
            "k1": [
                Profile.DY.value,
            ],
            "k2": [
                Profile.DY.value,
            ],
            "t5": [
                Profile.DY.value,
            ],
            "k3": [
                Profile.DY.value,
            ],
            "k4": [
                Profile.DY.value,
            ],
            "t6": [
                Profile.DY.value,
            ],
            "k5": [
                Profile.DY.value,
            ],
            "k6": [
                Profile.DY.value,
            ],
            "t7": [
                Profile.DY.value,
            ],
            "k7": [
                Profile.DY.value,
            ],
            "k8": [
                Profile.DY.value,
            ],
            "db1": [
                Profile.DY.value,
            ],
            "eps": [
                Profile.DY.value,
            ],
            "sdb1": [
                Profile.DY.value,
            ],
            "sdb2": [
                Profile.DY.value,
            ],
            "db2": [
                Profile.DY.value,
            ],
            "valve": [
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
