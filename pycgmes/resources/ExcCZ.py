"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcCZ(ExcitationSystemDynamics):
    """
    Czech proportion/integral exciter.

    kp: Regulator proportional gain (Kp).
    tc: Regulator integral time constant (Tc) (>= 0).
    vrmax: Voltage regulator maximum limit (Vrmax) (> ExcCZ.vrmin).
    vrmin: Voltage regulator minimum limit (Vrmin) (< ExcCZ.vrmax).
    ka: Regulator gain (Ka).
    ta: Regulator time constant (Ta) (>= 0).
    ke: Exciter constant related to self-excited field (Ke).
    te: Exciter time constant, integration rate associated with exciter control (Te) (>= 0).
    efdmax: Exciter output maximum limit (Efdmax) (> ExcCZ.efdmin).
    efdmin: Exciter output minimum limit (Efdmin) (< ExcCZ.efdmax).
    """

    kp: float = 0.0  # Type #PU in CIM
    tc: int = 0  # Type #Seconds in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    ka: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    ke: float = 0.0  # Type #PU in CIM
    te: int = 0  # Type #Seconds in CIM
    efdmax: float = 0.0  # Type #PU in CIM
    efdmin: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcCZ"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "kp": [
                Profile.DY.value,
            ],
            "tc": [
                Profile.DY.value,
            ],
            "vrmax": [
                Profile.DY.value,
            ],
            "vrmin": [
                Profile.DY.value,
            ],
            "ka": [
                Profile.DY.value,
            ],
            "ta": [
                Profile.DY.value,
            ],
            "ke": [
                Profile.DY.value,
            ],
            "te": [
                Profile.DY.value,
            ],
            "efdmax": [
                Profile.DY.value,
            ],
            "efdmin": [
                Profile.DY.value,
            ],
        }
