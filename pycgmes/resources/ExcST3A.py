"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcST3A(ExcitationSystemDynamics):
    """
    Modified IEEE ST3A static excitation system with added speed multiplier.

    vimax: Maximum voltage regulator input limit (Vimax) (> 0).  Typical value = 0,2.
    vimin: Minimum voltage regulator input limit (Vimin) (< 0).  Typical value = -0,2.
    kj: AVR gain (Kj) (> 0).  Typical value = 200.
    tb: Voltage regulator time constant (Tb) (>= 0).  Typical value = 6,67.
    tc: Voltage regulator time constant (Tc) (>= 0).  Typical value = 1.
    efdmax: Maximum AVR output (Efdmax) (>= 0).  Typical value = 6,9.
    km: Forward gain constant of the inner loop field regulator (Km) (> 0).  Typical value = 7,04.
    tm: Forward time constant of inner loop field regulator (Tm) (> 0).  Typical value = 1.
    vrmax: Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 1.
    vrmin: Minimum voltage regulator output (Vrmin) (< 0).  Typical value = -1.
    kg: Feedback gain constant of the inner loop field regulator (Kg) (>= 0).  Typical value = 1.
    kp: Potential source gain (Kp) (> 0).  Typical value = 4,37.
    thetap: Potential circuit phase angle (thetap).  Typical value = 20.
    ki: Potential circuit gain coefficient (Ki) (>= 0).  Typical value = 4,83.
    kc: Rectifier loading factor proportional to commutating reactance (Kc) (>= 0). Typical value = 1,1.
    xl: Reactance associated with potential source (Xl) (>= 0).  Typical value = 0,09.
    vbmax: Maximum excitation voltage (Vbmax) (> 0).  Typical value = 8,63.
    vgmax: Maximum inner loop feedback voltage (Vgmax) (>= 0).  Typical value = 6,53.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical value = 0.
    ks1: Coefficient to allow different usage of the model-speed coefficient (Ks1).  Typical value = 0.
    """

    vimax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vimin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kj: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tb: int = Field(
        default=0,
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

    efdmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    km: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tm: int = Field(
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

    kg: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    thetap: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ki: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    xl: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vbmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vgmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ks: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ks1: float = Field(
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
