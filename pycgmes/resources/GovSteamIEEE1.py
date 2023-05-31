"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass
class GovSteamIEEE1(TurbineGovernorDynamics):
    """
    IEEE steam turbine governor model. Reference: IEEE Transactions on Power Apparatus and Systems, November/December
      1973, Volume PAS-92, Number 6, Dynamic Models for Steam and Hydro Turbines in Power System Studies, page 1904.

    mwbase: Base for power values (MWbase) (> 0). Unit = MW.
    k: Governor gain (reciprocal of droop) (K) (> 0).  Typical value = 25.
    t1: Governor lag time constant (T1) (>= 0).  Typical value = 0.
    t2: Governor lead time constant (T2) (>= 0).  Typical value = 0.
    t3: Valve positioner time constant (T3) (> 0).  Typical value = 0,1.
    uo: Maximum valve opening velocity (Uo) (> 0).  Unit = PU / s.  Typical value = 1.
    uc: Maximum valve closing velocity (Uc) (< 0).  Unit = PU / s.  Typical value = -10.
    pmax: Maximum valve opening (Pmax) (> GovSteamIEEE1.pmin).  Typical value = 1.
    pmin: Minimum valve opening (Pmin) (>= 0 and < GovSteamIEEE1.pmax).  Typical value = 0.
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

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=GovSteamIEEE1\n"
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
            "k2": [
                self.profiles.DY.value,
            ],
            "t5": [
                self.profiles.DY.value,
            ],
            "k3": [
                self.profiles.DY.value,
            ],
            "k4": [
                self.profiles.DY.value,
            ],
            "t6": [
                self.profiles.DY.value,
            ],
            "k5": [
                self.profiles.DY.value,
            ],
            "k6": [
                self.profiles.DY.value,
            ],
            "t7": [
                self.profiles.DY.value,
            ],
            "k7": [
                self.profiles.DY.value,
            ],
            "k8": [
                self.profiles.DY.value,
            ],
        }
