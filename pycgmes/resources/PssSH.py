"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass(config=DataclassConfig)
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

        return "\n".join(
            ["class=PssSH"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "k": [
                Profile.DY.value,
            ],
            "k0": [
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
            "k4": [
                Profile.DY.value,
            ],
            "td": [
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
            "vsmax": [
                Profile.DY.value,
            ],
            "vsmin": [
                Profile.DY.value,
            ],
        }
