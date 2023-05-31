"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass
class GovHydroDD(TurbineGovernorDynamics):
    """
    Double derivative hydro governor and turbine.

    mwbase: Base for power values (MWbase) (>0).  Unit = MW.
    pmax: Maximum gate opening, PU of MWbase (Pmax) (> GovHydroDD.pmin).  Typical value = 1.
    pmin: Minimum gate opening, PU of MWbase (Pmin) (> GovHydroDD.pmax).  Typical value = 0.
    r: Steady state droop (R).  Typical value = 0,05.
    td: Input filter time constant (Td) (>= 0).  If = 0, block is bypassed.  Typical value = 0.
    tf: Washout time constant (Tf) (>= 0).  Typical value = 0,1.
    tp: Gate servo time constant (Tp) (>= 0).  If = 0, block is bypassed.  Typical value = 0,35.
    velop: Maximum gate opening velocity (Velop).  Unit = PU / s.  Typical value = 0,09.
    velcl: Maximum gate closing velocity (Velcl).  Unit = PU / s.  Typical value = -0,14.
    k1: Single derivative gain (K1).  Typical value = 3,6.
    k2: Double derivative gain (K2).  Typical value = 0,2.
    ki: Integral gain (Ki).  Typical value = 1.
    kg: Gate servo gain (Kg).  Typical value = 3.
    tturb: Turbine time constant (Tturb)  (>= 0).  See parameter detail 3.  Typical value = 0,8.
    aturb: Turbine numerator multiplier (Aturb) (see parameter detail 3).  Typical value = -1.
    bturb: Turbine denominator multiplier (Bturb) (see parameter detail 3).  Typical value = 0,5.
    tt: Power feedback time constant (Tt) (>= 0).  If = 0, block is bypassed.  Typical value = 0,02.
    db1: Intentional dead-band width (db1).  Unit = Hz.  Typical value = 0.
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
    gmax: Maximum gate opening (Gmax) (> GovHydroDD.gmin).  Typical value = 0.
    gmin: Minimum gate opening (Gmin) (< GovHydroDD.gmax).  Typical value = 0.
    inputSignal: Input signal switch (Flag).  true = Pe input is used false = feedback is received from CV. Flag is
      normally dependent on Tt.  If Tt is zero, Flag is set to false. If Tt is not zero, Flag is set to
      true.   Typical value = true.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    mwbase: float = 0.0  # Type #ActivePower in CIM
    pmax: float = 0.0  # Type #PU in CIM
    pmin: float = 0.0  # Type #PU in CIM
    r: float = 0.0  # Type #PU in CIM
    td: int = 0  # Type #Seconds in CIM
    tf: int = 0  # Type #Seconds in CIM
    tp: int = 0  # Type #Seconds in CIM
    velop: float = 0.0  # Type #Float in CIM
    velcl: float = 0.0  # Type #Float in CIM
    k1: float = 0.0  # Type #PU in CIM
    k2: float = 0.0  # Type #PU in CIM
    ki: float = 0.0  # Type #PU in CIM
    kg: float = 0.0  # Type #PU in CIM
    tturb: int = 0  # Type #Seconds in CIM
    aturb: float = 0.0  # Type #PU in CIM
    bturb: float = 0.0  # Type #PU in CIM
    tt: int = 0  # Type #Seconds in CIM
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
    gmax: float = 0.0  # Type #PU in CIM
    gmin: float = 0.0  # Type #PU in CIM
    inputSignal: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=GovHydroDD\n"
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
            "pmax": [
                self.profiles.DY.value,
            ],
            "pmin": [
                self.profiles.DY.value,
            ],
            "r": [
                self.profiles.DY.value,
            ],
            "td": [
                self.profiles.DY.value,
            ],
            "tf": [
                self.profiles.DY.value,
            ],
            "tp": [
                self.profiles.DY.value,
            ],
            "velop": [
                self.profiles.DY.value,
            ],
            "velcl": [
                self.profiles.DY.value,
            ],
            "k1": [
                self.profiles.DY.value,
            ],
            "k2": [
                self.profiles.DY.value,
            ],
            "ki": [
                self.profiles.DY.value,
            ],
            "kg": [
                self.profiles.DY.value,
            ],
            "tturb": [
                self.profiles.DY.value,
            ],
            "aturb": [
                self.profiles.DY.value,
            ],
            "bturb": [
                self.profiles.DY.value,
            ],
            "tt": [
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
            "gmax": [
                self.profiles.DY.value,
            ],
            "gmin": [
                self.profiles.DY.value,
            ],
            "inputSignal": [
                self.profiles.DY.value,
            ],
        }
