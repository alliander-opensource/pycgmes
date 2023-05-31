"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass
class GovHydro2(TurbineGovernorDynamics):
    """
    IEEE hydro turbine governor with straightforward penstock configuration and hydraulic-dashpot governor.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    tg: Gate servo time constant (Tg) (> 0).  Typical value = 0,5.
    tp: Pilot servo valve time constant (Tp) (>= 0).  Typical value = 0,03.
    uo: Maximum gate opening velocity (Uo).  Unit = PU / s.  Typical value = 0,1.
    uc: Maximum gate closing velocity (Uc) (< 0).  Unit = PU / s.   Typical value = -0,1.
    pmax: Maximum gate opening (Pmax) (> GovHydro2.pmin).  Typical value = 1.
    pmin: Minimum gate opening (Pmin) (< GovHydro2.pmax).  Typical value = 0.
    rperm: Permanent droop (Rperm).  Typical value = 0,05.
    rtemp: Temporary droop (Rtemp).  Typical value = 0,5.
    tr: Dashpot time constant (Tr) (>= 0).  Typical value = 12.
    tw: Water inertia time constant (Tw) (>= 0).  Typical value = 2.
    kturb: Turbine gain (Kturb).  Typical value = 1.
    aturb: Turbine numerator multiplier (Aturb).  Typical value = -1.
    bturb: Turbine denominator multiplier (Bturb) (> 0).  Typical value = 0,5.
    db1: Intentional deadband width (db1).  Unit = Hz.  Typical value = 0.
    eps: Intentional db hysteresis (eps).  Unit = Hz.  Typical value = 0.
    db2: Unintentional deadband (db2).  Unit = MW.  Typical value = 0.
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    mwbase: float = 0.0  # Type #ActivePower in CIM
    tg: int = 0  # Type #Seconds in CIM
    tp: int = 0  # Type #Seconds in CIM
    uo: float = 0.0  # Type #Float in CIM
    uc: float = 0.0  # Type #Float in CIM
    pmax: float = 0.0  # Type #PU in CIM
    pmin: float = 0.0  # Type #PU in CIM
    rperm: float = 0.0  # Type #PU in CIM
    rtemp: float = 0.0  # Type #PU in CIM
    tr: int = 0  # Type #Seconds in CIM
    tw: int = 0  # Type #Seconds in CIM
    kturb: float = 0.0  # Type #PU in CIM
    aturb: float = 0.0  # Type #PU in CIM
    bturb: float = 0.0  # Type #PU in CIM
    db1: float = 0.0  # Type #Frequency in CIM
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
        str_ = "class=GovHydro2\n"
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
            "tg": [
                self.profiles.DY.value,
            ],
            "tp": [
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
            "rperm": [
                self.profiles.DY.value,
            ],
            "rtemp": [
                self.profiles.DY.value,
            ],
            "tr": [
                self.profiles.DY.value,
            ],
            "tw": [
                self.profiles.DY.value,
            ],
            "kturb": [
                self.profiles.DY.value,
            ],
            "aturb": [
                self.profiles.DY.value,
            ],
            "bturb": [
                self.profiles.DY.value,
            ],
            "db1": [
                self.profiles.DY.value,
            ],
            "eps": [
                self.profiles.DY.value,
            ],
            "db2": [
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
