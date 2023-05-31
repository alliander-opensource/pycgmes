"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .TurbineGovernorDynamics import TurbineGovernorDynamics


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=GovSteamBB\n"
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
            "fcut": [
                self.profiles.DY.value,
            ],
            "ks": [
                self.profiles.DY.value,
            ],
            "kls": [
                self.profiles.DY.value,
            ],
            "kg": [
                self.profiles.DY.value,
            ],
            "t1": [
                self.profiles.DY.value,
            ],
            "kp": [
                self.profiles.DY.value,
            ],
            "tn": [
                self.profiles.DY.value,
            ],
            "kd": [
                self.profiles.DY.value,
            ],
            "td": [
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
            "k2": [
                self.profiles.DY.value,
            ],
            "t5": [
                self.profiles.DY.value,
            ],
            "k3": [
                self.profiles.DY.value,
            ],
            "t6": [
                self.profiles.DY.value,
            ],
            "peflag": [
                self.profiles.DY.value,
            ],
        }
