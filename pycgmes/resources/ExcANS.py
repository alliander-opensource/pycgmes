"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcANS(ExcitationSystemDynamics):
    """
    Italian excitation system. It represents static field voltage or excitation current feedback excitation system.

    k3: AVR gain (K3).  Typical value = 1000.
    k2: Exciter gain (K2).  Typical value = 20.
    kce: Ceiling factor (KCE).  Typical value = 1.
    t3: Time constant (T3) (>= 0).  Typical value = 1,6.
    t2: Time constant (T2) (>= 0).  Typical value = 0,05.
    t1: Time constant (T1) (>= 0).  Typical value = 20.
    blint: Governor control flag (BLINT).  0 = lead-lag regulator 1 = proportional integral regulator. Typical value =
      0.
    kvfif: Rate feedback signal flag (KVFIF).  0 = output voltage of the exciter 1 = exciter field current. Typical
      value = 0.
    ifmn: Minimum exciter current (IFMN).  Typical value = -5,2.
    ifmx: Maximum exciter current (IFMX).  Typical value = 6,5.
    vrmn: Minimum AVR output (VRMN).  Typical value = -5,2.
    vrmx: Maximum AVR output (VRMX).  Typical value = 6,5.
    krvecc: Feedback enabling (KRVECC).  0 = open loop control 1 = closed loop control. Typical value = 1.
    tb: Exciter time constant (TB) (>= 0).  Typical value = 0,04.
    """

    k3: float = 0.0  # Type #Float in CIM
    k2: float = 0.0  # Type #Float in CIM
    kce: float = 0.0  # Type #Float in CIM
    t3: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    t1: int = 0  # Type #Seconds in CIM
    blint: int = 0  # Type #Integer in CIM
    kvfif: int = 0  # Type #Integer in CIM
    ifmn: float = 0.0  # Type #PU in CIM
    ifmx: float = 0.0  # Type #PU in CIM
    vrmn: float = 0.0  # Type #PU in CIM
    vrmx: float = 0.0  # Type #PU in CIM
    krvecc: int = 0  # Type #Integer in CIM
    tb: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcANS"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "k3": [
                Profile.DY.value,
            ],
            "k2": [
                Profile.DY.value,
            ],
            "kce": [
                Profile.DY.value,
            ],
            "t3": [
                Profile.DY.value,
            ],
            "t2": [
                Profile.DY.value,
            ],
            "t1": [
                Profile.DY.value,
            ],
            "blint": [
                Profile.DY.value,
            ],
            "kvfif": [
                Profile.DY.value,
            ],
            "ifmn": [
                Profile.DY.value,
            ],
            "ifmx": [
                Profile.DY.value,
            ],
            "vrmn": [
                Profile.DY.value,
            ],
            "vrmx": [
                Profile.DY.value,
            ],
            "krvecc": [
                Profile.DY.value,
            ],
            "tb": [
                Profile.DY.value,
            ],
        }
