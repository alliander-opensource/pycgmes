"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
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

        return "\n".join(
            ["class=GovHydro1"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "rperm": [
                Profile.DY.value,
            ],
            "rtemp": [
                Profile.DY.value,
            ],
            "tr": [
                Profile.DY.value,
            ],
            "tf": [
                Profile.DY.value,
            ],
            "tg": [
                Profile.DY.value,
            ],
            "velm": [
                Profile.DY.value,
            ],
            "gmax": [
                Profile.DY.value,
            ],
            "gmin": [
                Profile.DY.value,
            ],
            "tw": [
                Profile.DY.value,
            ],
            "at": [
                Profile.DY.value,
            ],
            "dturb": [
                Profile.DY.value,
            ],
            "qnl": [
                Profile.DY.value,
            ],
            "hdam": [
                Profile.DY.value,
            ],
        }
