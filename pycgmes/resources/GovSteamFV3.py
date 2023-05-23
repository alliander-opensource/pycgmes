"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=GovSteamFV3\n"
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
            "mwbase": [
                self.profiles.DY.value,
            ],
            "k": [
                self.profiles.DY.value,
            ],
            "t1": [
                self.profiles.DY.value,
            ],
            "t2": [
                self.profiles.DY.value,
            ],
            "t3": [
                self.profiles.DY.value,
            ],
            "uo": [
                self.profiles.DY.value,
            ],
            "uc": [
                self.profiles.DY.value,
            ],
            "pmax": [
                self.profiles.DY.value,
            ],
            "pmin": [
                self.profiles.DY.value,
            ],
            "t4": [
                self.profiles.DY.value,
            ],
            "k1": [
                self.profiles.DY.value,
            ],
            "t5": [
                self.profiles.DY.value,
            ],
            "k2": [
                self.profiles.DY.value,
            ],
            "t6": [
                self.profiles.DY.value,
            ],
            "k3": [
                self.profiles.DY.value,
            ],
            "ta": [
                self.profiles.DY.value,
            ],
            "tb": [
                self.profiles.DY.value,
            ],
            "tc": [
                self.profiles.DY.value,
            ],
            "prmax": [
                self.profiles.DY.value,
            ],
            "gv1": [
                self.profiles.DY.value,
            ],
            "pgv1": [
                self.profiles.DY.value,
            ],
            "gv2": [
                self.profiles.DY.value,
            ],
            "pgv2": [
                self.profiles.DY.value,
            ],
            "gv3": [
                self.profiles.DY.value,
            ],
            "pgv3": [
                self.profiles.DY.value,
            ],
            "gv4": [
                self.profiles.DY.value,
            ],
            "pgv4": [
                self.profiles.DY.value,
            ],
            "gv5": [
                self.profiles.DY.value,
            ],
            "pgv5": [
                self.profiles.DY.value,
            ],
            "gv6": [
                self.profiles.DY.value,
            ],
            "pgv6": [
                self.profiles.DY.value,
            ],
        }
