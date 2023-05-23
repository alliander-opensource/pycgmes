"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcAVR3(ExcitationSystemDynamics):
    """
    Italian excitation system. It represents an exciter dynamo and electric regulator.

    ka: AVR gain (KA).  Typical value = 100.
    vrmn: Minimum AVR output (VRMN).  Typical value = -7,5.
    vrmx: Maximum AVR output (VRMX).  Typical value = 7,5.
    t1: AVR time constant (T1) (>= 0).  Typical value = 20.
    t2: AVR time constant (T2) (>= 0).  Typical value = 1,6.
    t3: AVR time constant (T3) (>= 0).  Typical value = 0,66.
    t4: AVR time constant (T4) (>= 0).  Typical value = 0,07.
    te: Exciter time constant (TE) (>= 0).  Typical value = 1.
    e1: Field voltage value 1 (E1).  Typical value = 4,18.
    se1: Saturation factor at E1 (S[E1]).  Typical value = 0,1.
    e2: Field voltage value 2 (E2).  Typical value = 3,14.
    se2: Saturation factor at E2 (S[E2]).  Typical value = 0,03.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ka: float = 0.0  # Type #Float in CIM
    vrmn: float = 0.0  # Type #PU in CIM
    vrmx: float = 0.0  # Type #PU in CIM
    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    t4: int = 0  # Type #Seconds in CIM
    te: int = 0  # Type #Seconds in CIM
    e1: float = 0.0  # Type #PU in CIM
    se1: float = 0.0  # Type #Float in CIM
    e2: float = 0.0  # Type #PU in CIM
    se2: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExcAVR3\n"
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
        }
