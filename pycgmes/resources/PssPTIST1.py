"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass(config=DataclassConfig)
class PssPTIST1(PowerSystemStabilizerDynamics):
    """
    PTI microprocessor-based stabilizer type 1.

    m: (M).  M = 2 x H.  Typical value = 5.
    tf: Time constant (Tf) (>= 0).  Typical value = 0,2.
    tp: Time constant (Tp) (>= 0).  Typical value = 0,2.
    t1: Time constant (T1) (>= 0).  Typical value = 0,3.
    t2: Time constant (T2) (>= 0).  Typical value = 1.
    t3: Time constant (T3) (>= 0).  Typical value = 0,2.
    t4: Time constant (T4) (>= 0).  Typical value = 0,05.
    k: Gain (K).  Typical value = 9.
    dtf: Time step frequency calculation (deltatf) (>= 0).  Typical value = 0,025.
    dtc: Time step related to activation of controls (deltatc) (>= 0).  Typical value = 0,025.
    dtp: Time step active power calculation (deltatp) (>= 0).  Typical value = 0,0125.
    """

    m: float = 0.0  # Type #PU in CIM
    tf: int = 0  # Type #Seconds in CIM
    tp: int = 0  # Type #Seconds in CIM
    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    t4: int = 0  # Type #Seconds in CIM
    k: float = 0.0  # Type #PU in CIM
    dtf: int = 0  # Type #Seconds in CIM
    dtc: int = 0  # Type #Seconds in CIM
    dtp: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PssPTIST1"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "m": [
                Profile.DY.value,
            ],
            "tf": [
                Profile.DY.value,
            ],
            "tp": [
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
            "k": [
                Profile.DY.value,
            ],
            "dtf": [
                Profile.DY.value,
            ],
            "dtc": [
                Profile.DY.value,
            ],
            "dtp": [
                Profile.DY.value,
            ],
        }
