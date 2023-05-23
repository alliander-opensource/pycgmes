"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass
class PssSB4(PowerSystemStabilizerDynamics):
    """
    Power sensitive stabilizer model.

    tt: Time constant (Tt) (>= 0).  Typical value = 0,18.
    kx: Gain (Kx).  Typical value = 2,7.
    tx2: Time constant (Tx2) (>= 0).  Typical value = 5,0.
    ta: Time constant (Ta) (>= 0).  Typical value = 0,37.
    tx1: Reset time constant (Tx1) (>= 0).  Typical value = 0,035.
    tb: Time constant (Tb) (>= 0).  Typical value = 0,37.
    tc: Time constant (Tc) (>= 0).  Typical value = 0,035.
    td: Time constant (Td) (>= 0).  Typical value = 0,0.
    te: Time constant (Te) (>= 0).  Typical value = 0,0169.
    vsmax: Limiter (Vsmax) (> PssSB4.vsmin).  Typical value = 0,062.
    vsmin: Limiter (Vsmin) (< PssSB4.vsmax).  Typical value = -0,062.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    tt: int = 0  # Type #Seconds in CIM
    kx: float = 0.0  # Type #PU in CIM
    tx2: int = 0  # Type #Seconds in CIM
    ta: int = 0  # Type #Seconds in CIM
    tx1: int = 0  # Type #Seconds in CIM
    tb: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM
    td: int = 0  # Type #Seconds in CIM
    te: int = 0  # Type #Seconds in CIM
    vsmax: float = 0.0  # Type #PU in CIM
    vsmin: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PssSB4\n"
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
            "tt": [
                self.profiles.DY.value,
            ],
            "kx": [
                self.profiles.DY.value,
            ],
            "tx2": [
                self.profiles.DY.value,
            ],
            "ta": [
                self.profiles.DY.value,
            ],
            "tx1": [
                self.profiles.DY.value,
            ],
            "tb": [
                self.profiles.DY.value,
            ],
            "tc": [
                self.profiles.DY.value,
            ],
            "td": [
                self.profiles.DY.value,
            ],
            "te": [
                self.profiles.DY.value,
            ],
            "vsmax": [
                self.profiles.DY.value,
            ],
            "vsmin": [
                self.profiles.DY.value,
            ],
        }
