"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcAVR2(ExcitationSystemDynamics):
    """
    Italian excitation system corresponding to IEEE (1968) type 2 model. It represents an alternator and rotating diodes
      and electromechanic voltage regulators.

    ka: AVR gain (KA).  Typical value = 500.
    vrmn: Minimum AVR output (VRMN).  Typical value = -6.
    vrmx: Maximum AVR output (VRMX).  Typical value = 7.
    ta: AVR time constant (TA) (>= 0).  Typical value = 0,02.
    tb: AVR time constant (TB) (>= 0).  Typical value = 0.
    te: Exciter time constant (TE) (>= 0).  Typical value = 1.
    e1: Field voltage value 1 (E1).  Typical value = 4,18.
    se1: Saturation factor at E1 (S[E1]).  Typical value = 0.1.
    e2: Field voltage value 2 (E2).  Typical value = 3,14.
    se2: Saturation factor at E2 (S[E2]).  Typical value = 0,03.
    kf: Rate feedback gain (KF).  Typical value = 0,12.
    tf1: Rate feedback time constant (TF1) (>= 0).  Typical value = 1.
    tf2: Rate feedback time constant (TF2) (>= 0).  Typical value = 1.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ka: float = 0.0  # Type #Float in CIM
    vrmn: float = 0.0  # Type #PU in CIM
    vrmx: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    tb: int = 0  # Type #Seconds in CIM
    te: int = 0  # Type #Seconds in CIM
    e1: float = 0.0  # Type #PU in CIM
    se1: float = 0.0  # Type #Float in CIM
    e2: float = 0.0  # Type #PU in CIM
    se2: float = 0.0  # Type #Float in CIM
    kf: float = 0.0  # Type #Float in CIM
    tf1: int = 0  # Type #Seconds in CIM
    tf2: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExcAVR2\n"
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
            "ka": [
                self.profiles.DY.value,
            ],
            "vrmn": [
                self.profiles.DY.value,
            ],
            "vrmx": [
                self.profiles.DY.value,
            ],
            "ta": [
                self.profiles.DY.value,
            ],
            "tb": [
                self.profiles.DY.value,
            ],
            "te": [
                self.profiles.DY.value,
            ],
            "e1": [
                self.profiles.DY.value,
            ],
            "se1": [
                self.profiles.DY.value,
            ],
            "e2": [
                self.profiles.DY.value,
            ],
            "se2": [
                self.profiles.DY.value,
            ],
            "kf": [
                self.profiles.DY.value,
            ],
            "tf1": [
                self.profiles.DY.value,
            ],
            "tf2": [
                self.profiles.DY.value,
            ],
        }
