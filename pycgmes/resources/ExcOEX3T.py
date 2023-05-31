"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcOEX3T(ExcitationSystemDynamics):
    """
    Modified IEEE type ST1 excitation system with semi-continuous and acting terminal voltage limiter.

    t1: Time constant (T1) (>= 0).
    t2: Time constant (T2) (>= 0).
    t3: Time constant (T3) (>= 0).
    t4: Time constant (T4) (>= 0).
    ka: Gain (KA).
    t5: Time constant (T5) (>= 0).
    t6: Time constant (T6) (>= 0).
    vrmax: Limiter (VRMAX) (> ExcOEX3T.vrmin).
    vrmin: Limiter (VRMIN) (< ExcOEX3T.vrmax).
    te: Time constant (TE) (>= 0).
    kf: Gain (KF).
    tf: Time constant (TF) (>= 0).
    kc: Gain (KC).
    kd: Gain (KD).
    ke: Gain (KE).
    e1: Saturation parameter (E1).
    see1: Saturation parameter (SE[E1]).
    e2: Saturation parameter (E2).
    see2: Saturation parameter (SE[E2]).
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    t4: int = 0  # Type #Seconds in CIM
    ka: float = 0.0  # Type #PU in CIM
    t5: int = 0  # Type #Seconds in CIM
    t6: int = 0  # Type #Seconds in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    te: int = 0  # Type #Seconds in CIM
    kf: float = 0.0  # Type #PU in CIM
    tf: int = 0  # Type #Seconds in CIM
    kc: float = 0.0  # Type #PU in CIM
    kd: float = 0.0  # Type #PU in CIM
    ke: float = 0.0  # Type #PU in CIM
    e1: float = 0.0  # Type #PU in CIM
    see1: float = 0.0  # Type #PU in CIM
    e2: float = 0.0  # Type #PU in CIM
    see2: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExcOEX3T\n"
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
            "t1": [
                self.profiles.DY.value,
            ],
            "t2": [
                self.profiles.DY.value,
            ],
            "t3": [
                self.profiles.DY.value,
            ],
            "t4": [
                self.profiles.DY.value,
            ],
            "ka": [
                self.profiles.DY.value,
            ],
            "t5": [
                self.profiles.DY.value,
            ],
            "t6": [
                self.profiles.DY.value,
            ],
            "vrmax": [
                self.profiles.DY.value,
            ],
            "vrmin": [
                self.profiles.DY.value,
            ],
            "te": [
                self.profiles.DY.value,
            ],
            "kf": [
                self.profiles.DY.value,
            ],
            "tf": [
                self.profiles.DY.value,
            ],
            "kc": [
                self.profiles.DY.value,
            ],
            "kd": [
                self.profiles.DY.value,
            ],
            "ke": [
                self.profiles.DY.value,
            ],
            "e1": [
                self.profiles.DY.value,
            ],
            "see1": [
                self.profiles.DY.value,
            ],
            "e2": [
                self.profiles.DY.value,
            ],
            "see2": [
                self.profiles.DY.value,
            ],
        }
