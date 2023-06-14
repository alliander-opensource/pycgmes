"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics


@dataclass(config=DataclassConfig)
class UnderexcLimX2(UnderexcitationLimiterDynamics):
    """
    Westinghouse minimum excitation limiter.

    kf2: Differential gain (KF2).
    tf2: Differential time constant (TF2) (>= 0).
    km: Minimum excitation limit gain (KM).
    tm: Minimum excitation limit time constant (TM) (>= 0).
    melmax: Minimum excitation limit value (MELMAX).
    qo: Excitation centre setting (QO).
    r: Excitation radius (R).
    """

    kf2: float = 0.0  # Type #PU in CIM
    tf2: int = 0  # Type #Seconds in CIM
    km: float = 0.0  # Type #PU in CIM
    tm: int = 0  # Type #Seconds in CIM
    melmax: float = 0.0  # Type #PU in CIM
    qo: float = 0.0  # Type #PU in CIM
    r: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=UnderexcLimX2"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "kf2": [
                Profile.DY.value,
            ],
            "tf2": [
                Profile.DY.value,
            ],
            "km": [
                Profile.DY.value,
            ],
            "tm": [
                Profile.DY.value,
            ],
            "melmax": [
                Profile.DY.value,
            ],
            "qo": [
                Profile.DY.value,
            ],
            "r": [
                Profile.DY.value,
            ],
        }
