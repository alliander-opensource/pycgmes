"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass(config=DataclassConfig)
class GovSteamBB(TurbineGovernorDynamics):
    """
    European governor model.

    fcut: Frequency deadband (fcut) (>= 0).  Typical value = 0,002.
    ks: Gain (Ks).  Typical value = 21,0.
    kls: Gain (Kls) (> 0).  Typical value = 0,1.
    kg: Gain (Kg).  Typical value = 1,0.
    t1: Time constant (T1).  Typical value = 0,05.
    kp: Gain (Kp).  Typical value = 1,0.
    tn: Time constant (Tn) (> 0).  Typical value = 1,0.
    kd: Gain (Kd).  Typical value = 1,0.
    td: Time constant (Td) (> 0).  Typical value = 1,0.
    pmax: High power limit (Pmax) (> GovSteamBB.pmin).  Typical value = 1,0.
    pmin: Low power limit (Pmin) (< GovSteamBB.pmax).  Typical value = 0.
    t4: Time constant (T4).  Typical value = 0,15.
    k2: Gain (K2).  Typical value = 0,75.
    t5: Time constant (T5).  Typical value = 12,0.
    k3: Gain (K3).  Typical value = 0,5.
    t6: Time constant (T6).  Typical value = 0,75.
    peflag: Electric power input selection (Peflag).   true = electric power input false = feedback signal. Typical
      value = false.
    """

    fcut: float = 0.0  # Type #PU in CIM
    ks: float = 0.0  # Type #PU in CIM
    kls: float = 0.0  # Type #PU in CIM
    kg: float = 0.0  # Type #PU in CIM
    t1: int = 0  # Type #Seconds in CIM
    kp: float = 0.0  # Type #PU in CIM
    tn: int = 0  # Type #Seconds in CIM
    kd: float = 0.0  # Type #PU in CIM
    td: int = 0  # Type #Seconds in CIM
    pmax: float = 0.0  # Type #PU in CIM
    pmin: float = 0.0  # Type #PU in CIM
    t4: int = 0  # Type #Seconds in CIM
    k2: float = 0.0  # Type #PU in CIM
    t5: int = 0  # Type #Seconds in CIM
    k3: float = 0.0  # Type #PU in CIM
    t6: int = 0  # Type #Seconds in CIM
    peflag: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=GovSteamBB"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "fcut": [
                Profile.DY.value,
            ],
            "ks": [
                Profile.DY.value,
            ],
            "kls": [
                Profile.DY.value,
            ],
            "kg": [
                Profile.DY.value,
            ],
            "t1": [
                Profile.DY.value,
            ],
            "kp": [
                Profile.DY.value,
            ],
            "tn": [
                Profile.DY.value,
            ],
            "kd": [
                Profile.DY.value,
            ],
            "td": [
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
            "k2": [
                Profile.DY.value,
            ],
            "t5": [
                Profile.DY.value,
            ],
            "k3": [
                Profile.DY.value,
            ],
            "t6": [
                Profile.DY.value,
            ],
            "peflag": [
                Profile.DY.value,
            ],
        }
