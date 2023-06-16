"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovSteamFV3(TurbineGovernorDynamics):
    """
    Simplified GovSteamIEEE1 steam turbine governor with Prmax limit and fast valving.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    k: Governor gain, (reciprocal of droop) (K).  Typical value = 20.
    t1: Governor lead time constant (T1) (>= 0).  Typical value = 0.
    t2: Governor lag time constant (T2) (>= 0).  Typical value = 0.
    t3: Valve positioner time constant (T3) (> 0).  Typical value = 0.
    uo: Maximum valve opening velocity (Uo).  Unit = PU / s.  Typical value = 0,1.
    uc: Maximum valve closing velocity (Uc).  Unit = PU / s.  Typical value = -1.
    pmax: Maximum valve opening, PU of MWbase (Pmax) (> GovSteamFV3.pmin).  Typical value = 1.
    pmin: Minimum valve opening, PU of MWbase (Pmin) (< GovSteamFV3.pmax).  Typical value = 0.
    t4: Inlet piping/steam bowl time constant (T4) (>= 0).  Typical value = 0,2.
    k1: Fraction of turbine power developed after first boiler pass (K1).  Typical value = 0,2.
    t5: Time constant of second boiler pass (i.e. reheater) (T5) (> 0 if fast valving is used, otherwise >= 0).  Typical
      value = 0,5.
    k2: Fraction of turbine power developed after second boiler pass (K2).  Typical value = 0,2.
    t6: Time constant of crossover or third boiler pass (T6) (>= 0).  Typical value = 10.
    k3: Fraction of hp turbine power developed after crossover or third boiler pass (K3). Typical value = 0,6.
    ta: Time to close intercept valve (IV) (Ta) (>= 0).  Typical value = 0,97.
    tb: Time until IV starts to reopen (Tb) (>= 0).  Typical value = 0,98.
    tc: Time until IV is fully open (Tc) (>= 0).  Typical value = 0,99.
    prmax: Max. pressure in reheater (Prmax).  Typical value = 1.
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
    k1: float = 0.0  # Type #PU in CIM
    t5: int = 0  # Type #Seconds in CIM
    k2: float = 0.0  # Type #PU in CIM
    t6: int = 0  # Type #Seconds in CIM
    k3: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    tb: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM
    prmax: float = 0.0  # Type #PU in CIM
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
            ["class=GovSteamFV3"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "t5": [
                Profile.DY.value,
            ],
            "k2": [
                Profile.DY.value,
            ],
            "t6": [
                Profile.DY.value,
            ],
            "k3": [
                Profile.DY.value,
            ],
            "ta": [
                Profile.DY.value,
            ],
            "tb": [
                Profile.DY.value,
            ],
            "tc": [
                Profile.DY.value,
            ],
            "prmax": [
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
