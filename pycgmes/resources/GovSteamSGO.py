"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovSteamSGO(TurbineGovernorDynamics):
    """
    Simplified steam turbine governor.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    t1: Controller lag (T1) (>= 0).
    t2: Controller lead compensation (T2) (>= 0).
    t3: Governor lag (T3) (> 0).
    t4: Delay due to steam inlet volumes associated with steam chest and inlet piping (T4) (>= 0).
    t5: Reheater delay including hot and cold leads (T5) (>= 0).
    t6: Delay due to IP-LP turbine, crossover pipes and LP end hoods (T6) (>= 0).
    k1: One / PU regulation (K1).
    k2: Fraction (K2).
    k3: Fraction (K3).
    pmax: Upper power limit (Pmax) (> GovSteamSGO.pmin).
    pmin: Lower power limit (Pmin) (>= 0 and < GovSteamSGO.pmax).
    """

    mwbase: float = 0.0  # Type #ActivePower in CIM
    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    t4: int = 0  # Type #Seconds in CIM
    t5: int = 0  # Type #Seconds in CIM
    t6: int = 0  # Type #Seconds in CIM
    k1: float = 0.0  # Type #PU in CIM
    k2: float = 0.0  # Type #PU in CIM
    k3: float = 0.0  # Type #PU in CIM
    pmax: float = 0.0  # Type #PU in CIM
    pmin: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=GovSteamSGO"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "t1": [
                Profile.DY.value,
            ],
            "t2": [
                Profile.DY.value,
            ],
            "t3": [
                Profile.DY.value,
            ],
            "t4": [
                Profile.DY.value,
            ],
            "t5": [
                Profile.DY.value,
            ],
            "t6": [
                Profile.DY.value,
            ],
            "k1": [
                Profile.DY.value,
            ],
            "k2": [
                Profile.DY.value,
            ],
            "k3": [
                Profile.DY.value,
            ],
            "pmax": [
                Profile.DY.value,
            ],
            "pmin": [
                Profile.DY.value,
            ],
        }
