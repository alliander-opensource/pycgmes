"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass
class GovHydro1(TurbineGovernorDynamics):
    """
    Basic hydro turbine governor.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    rperm: Permanent droop (R) (> 0).  Typical value = 0,04.
    rtemp: Temporary droop (r) (> GovHydro1.rperm).  Typical value = 0,3.
    tr: Washout time constant (Tr) (> 0).  Typical value = 5.
    tf: Filter time constant (Tf) (> 0).  Typical value = 0,05.
    tg: Gate servo time constant (Tg) (> 0).  Typical value = 0,5.
    velm: Maximum gate velocity (Vlem) (> 0).  Typical value = 0,2.
    gmax: Maximum gate opening (Gmax) (> 0 and > GovHydro.gmin).  Typical value = 1.
    gmin: Minimum gate opening (Gmin) (>= 0 and < GovHydro1.gmax).  Typical value = 0.
    tw: Water inertia time constant (Tw) (> 0).  Typical value = 1.
    at: Turbine gain (At) (> 0).  Typical value = 1,2.
    dturb: Turbine damping factor (Dturb) (>= 0).  Typical value = 0,5.
    qnl: No-load flow at nominal head (qnl) (>= 0).  Typical value = 0,08.
    hdam: Turbine nominal head (hdam).  Typical value = 1.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    mwbase: float = 0.0  # Type #ActivePower in CIM
    rperm: float = 0.0  # Type #PU in CIM
    rtemp: float = 0.0  # Type #PU in CIM
    tr: int = 0  # Type #Seconds in CIM
    tf: int = 0  # Type #Seconds in CIM
    tg: int = 0  # Type #Seconds in CIM
    velm: float = 0.0  # Type #Float in CIM
    gmax: float = 0.0  # Type #PU in CIM
    gmin: float = 0.0  # Type #PU in CIM
    tw: int = 0  # Type #Seconds in CIM
    at: float = 0.0  # Type #PU in CIM
    dturb: float = 0.0  # Type #PU in CIM
    qnl: float = 0.0  # Type #PU in CIM
    hdam: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=GovHydro1\n"
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
            "rperm": [
                self.profiles.DY.value,
            ],
            "rtemp": [
                self.profiles.DY.value,
            ],
            "tr": [
                self.profiles.DY.value,
            ],
            "tf": [
                self.profiles.DY.value,
            ],
            "tg": [
                self.profiles.DY.value,
            ],
            "velm": [
                self.profiles.DY.value,
            ],
            "gmax": [
                self.profiles.DY.value,
            ],
            "gmin": [
                self.profiles.DY.value,
            ],
            "tw": [
                self.profiles.DY.value,
            ],
            "at": [
                self.profiles.DY.value,
            ],
            "dturb": [
                self.profiles.DY.value,
            ],
            "qnl": [
                self.profiles.DY.value,
            ],
            "hdam": [
                self.profiles.DY.value,
            ],
        }
