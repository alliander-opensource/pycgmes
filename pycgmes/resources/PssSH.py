"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass
class PssSH(PowerSystemStabilizerDynamics):
    """
    SiemensTM "H infinity" power system stabilizer with generator electrical power input. [Footnote: Siemens "H
      infinity" power system stabilizers are an example of suitable products available commercially. This
      information is given for the convenience of users of this document and does not constitute an endorsement by
      IEC of these products.]

    k: Main gain (K).  Typical value = 1.
    k0: Gain 0 (K0).  Typical value = 0,012.
    k1: Gain 1 (K1).  Typical value = 0,488.
    k2: Gain 2 (K2).  Typical value = 0,064.
    k3: Gain 3 (K3).  Typical value = 0,224.
    k4: Gain 4 (K4).  Typical value = 0,1.
    td: Input time constant (Td) (>= 0).  Typical value = 10.
    t1: Time constant 1 (T1) (> 0).  Typical value = 0,076.
    t2: Time constant 2 (T2) (> 0).  Typical value = 0,086.
    t3: Time constant 3 (T3) (> 0).   Typical value = 1,068.
    t4: Time constant 4 (T4) (> 0).  Typical value = 1,913.
    vsmax: Output maximum limit (Vsmax) (> PssSH.vsmin).  Typical value = 0,1.
    vsmin: Output minimum limit (Vsmin) (< PssSH.vsmax).  Typical value = -0,1.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    k: float = 0.0  # Type #PU in CIM
    k0: float = 0.0  # Type #PU in CIM
    k1: float = 0.0  # Type #PU in CIM
    k2: float = 0.0  # Type #PU in CIM
    k3: float = 0.0  # Type #PU in CIM
    k4: float = 0.0  # Type #PU in CIM
    td: int = 0  # Type #Seconds in CIM
    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    t4: int = 0  # Type #Seconds in CIM
    vsmax: float = 0.0  # Type #PU in CIM
    vsmin: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PssSH\n"
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
            "k": [
                self.profiles.DY.value,
            ],
            "k0": [
                self.profiles.DY.value,
            ],
            "k1": [
                self.profiles.DY.value,
            ],
            "k2": [
                self.profiles.DY.value,
            ],
            "k3": [
                self.profiles.DY.value,
            ],
            "k4": [
                self.profiles.DY.value,
            ],
            "td": [
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
            "vsmax": [
                self.profiles.DY.value,
            ],
            "vsmin": [
                self.profiles.DY.value,
            ],
        }
