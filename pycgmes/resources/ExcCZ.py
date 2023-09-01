"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
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

    kp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tc: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vrmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vrmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ka: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ta: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ke: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    te: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efdmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efdmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
