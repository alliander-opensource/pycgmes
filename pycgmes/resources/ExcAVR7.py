"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcAVR7(ExcitationSystemDynamics):
    """
    IVO excitation system.

    k1: Gain (K1).  Typical value = 1.
    a1: Lead coefficient (A1).  Typical value = 0,5.
    a2: Lag coefficient (A2).  Typical value = 0,5.
    t1: Lead time constant (T1) (>= 0).  Typical value = 0,05.
    t2: Lag time constant (T2) (>= 0).  Typical value = 0,1.
    vmax1: Lead-lag maximum limit (Vmax1) (> ExcAVR7.vmin1).  Typical value = 5.
    vmin1: Lead-lag minimum limit (Vmin1) (< ExcAVR7.vmax1).  Typical value = -5.
    k3: Gain (K3).  Typical value = 3.
    a3: Lead coefficient (A3).  Typical value = 0,5.
    a4: Lag coefficient (A4).  Typical value = 0,5.
    t3: Lead time constant (T3) (>= 0).  Typical value = 0,1.
    t4: Lag time constant (T4) (>= 0).  Typical value = 0,1.
    vmax3: Lead-lag maximum limit (Vmax3) (> ExcAVR7.vmin3).  Typical value = 5.
    vmin3: Lead-lag minimum limit (Vmin3) (< ExcAVR7.vmax3).  Typical value = -5.
    k5: Gain (K5).  Typical value = 1.
    a5: Lead coefficient (A5).  Typical value = 0,5.
    a6: Lag coefficient (A6).  Typical value = 0,5.
    t5: Lead time constant (T5) (>= 0).  Typical value = 0,1.
    t6: Lag time constant (T6) (>= 0).  Typical value = 0,1.
    vmax5: Lead-lag maximum limit (Vmax5) (> ExcAVR7.vmin5).  Typical value = 5.
    vmin5: Lead-lag minimum limit (Vmin5) (< ExcAVR7.vmax5).  Typical value = -2.
    """

    k1: float = 0.0  # Type #PU in CIM
    a1: float = 0.0  # Type #PU in CIM
    a2: float = 0.0  # Type #PU in CIM
    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    vmax1: float = 0.0  # Type #PU in CIM
    vmin1: float = 0.0  # Type #PU in CIM
    k3: float = 0.0  # Type #PU in CIM
    a3: float = 0.0  # Type #PU in CIM
    a4: float = 0.0  # Type #PU in CIM
    t3: int = 0  # Type #Seconds in CIM
    t4: int = 0  # Type #Seconds in CIM
    vmax3: float = 0.0  # Type #PU in CIM
    vmin3: float = 0.0  # Type #PU in CIM
    k5: float = 0.0  # Type #PU in CIM
    a5: float = 0.0  # Type #PU in CIM
    a6: float = 0.0  # Type #PU in CIM
    t5: int = 0  # Type #Seconds in CIM
    t6: int = 0  # Type #Seconds in CIM
    vmax5: float = 0.0  # Type #PU in CIM
    vmin5: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcAVR7"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "k1": [
                Profile.DY.value,
            ],
            "a1": [
                Profile.DY.value,
            ],
            "a2": [
                Profile.DY.value,
            ],
            "t1": [
                Profile.DY.value,
            ],
            "t2": [
                Profile.DY.value,
            ],
            "vmax1": [
                Profile.DY.value,
            ],
            "vmin1": [
                Profile.DY.value,
            ],
            "k3": [
                Profile.DY.value,
            ],
            "a3": [
                Profile.DY.value,
            ],
            "a4": [
                Profile.DY.value,
            ],
            "t3": [
                Profile.DY.value,
            ],
            "t4": [
                Profile.DY.value,
            ],
            "vmax3": [
                Profile.DY.value,
            ],
            "vmin3": [
                Profile.DY.value,
            ],
            "k5": [
                Profile.DY.value,
            ],
            "a5": [
                Profile.DY.value,
            ],
            "a6": [
                Profile.DY.value,
            ],
            "t5": [
                Profile.DY.value,
            ],
            "t6": [
                Profile.DY.value,
            ],
            "vmax5": [
                Profile.DY.value,
            ],
            "vmin5": [
                Profile.DY.value,
            ],
        }
