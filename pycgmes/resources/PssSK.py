"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass
class PssSK(PowerSystemStabilizerDynamics):
    """
    Slovakian PSS with three inputs.

    k1: Gain P (K1).  Typical value = -0,3.
    k2: Gain fE (K2).  Typical value = -0,15.
    k3: Gain If (K3).  Typical value = 10.
    t1: Denominator time constant (T1) (> 0,005).  Typical value = 0,3.
    t2: Filter time constant (T2) (> 0,005).  Typical value = 0,35.
    t3: Denominator time constant (T3) (> 0,005).  Typical value = 0,22.
    t4: Filter time constant (T4) (> 0,005).  Typical value = 0,02.
    t5: Denominator time constant (T5) (> 0,005).  Typical value = 0,02.
    t6: Filter time constant (T6) (> 0,005).  Typical value = 0,02.
    vsmax: Stabilizer output maximum limit (VSMAX) (> PssSK.vsmin).  Typical value = 0,4.
    vsmin: Stabilizer output minimum limit (VSMIN) (< PssSK.vsmax).  Typical value = -0.4.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    k1: float = 0.0  # Type #PU in CIM
    k2: float = 0.0  # Type #PU in CIM
    k3: float = 0.0  # Type #PU in CIM
    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    t4: int = 0  # Type #Seconds in CIM
    t5: int = 0  # Type #Seconds in CIM
    t6: int = 0  # Type #Seconds in CIM
    vsmax: float = 0.0  # Type #PU in CIM
    vsmin: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PssSK\n"
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
            "k1": [
                self.profiles.DY.value,
            ],
            "k2": [
                self.profiles.DY.value,
            ],
            "k3": [
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
            "t5": [
                self.profiles.DY.value,
            ],
            "t6": [
                self.profiles.DY.value,
            ],
            "vsmax": [
                self.profiles.DY.value,
            ],
            "vsmin": [
                self.profiles.DY.value,
            ],
        }
