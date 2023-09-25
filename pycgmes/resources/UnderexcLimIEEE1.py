"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics


@dataclass(config=DataclassConfig)
class UnderexcLimIEEE1(UnderexcitationLimiterDynamics):
    """
    Type UEL1 model which has a circular limit boundary when plotted in terms of machine reactive power vs. real power
      output. Reference: IEEE UEL1 421.5-2005, 10.1.

    kur: UEL radius setting (KUR).  Typical value = 1,95.
    kuc: UEL centre setting (KUC).  Typical value = 1,38.
    kuf: UEL excitation system stabilizer gain (KUF).  Typical value = 3,3.
    vurmax: UEL maximum limit for radius phasor magnitude (VURMAX).  Typical value = 5,8.
    vucmax: UEL maximum limit for operating point phasor magnitude (VUCMAX).  Typical value = 5,8.
    kui: UEL integral gain (KUI).  Typical value = 0.
    kul: UEL proportional gain (KUL).  Typical value = 100.
    vuimax: UEL integrator output maximum limit (VUIMAX) (> UnderexcLimIEEE1.vuimin).
    vuimin: UEL integrator output minimum limit (VUIMIN) (< UnderexcLimIEEE1.vuimax).
    tu1: UEL lead time constant (TU1) (>= 0).  Typical value = 0.
    tu2: UEL lag time constant (TU2) (>= 0).  Typical value = 0,05.
    tu3: UEL lead time constant (TU3) (>= 0).  Typical value = 0.
    tu4: UEL lag time constant (TU4) (>= 0).  Typical value = 0.
    vulmax: UEL output maximum limit (VULMAX) (> UnderexcLimIEEE1.vulmin).  Typical value = 18.
    vulmin: UEL output minimum limit (VULMIN) (< UnderexcLimIEEE1.vulmax).  Typical value = -18.
    """

    kur: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kuc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kuf: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vurmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vucmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kui: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kul: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vuimax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vuimin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tu1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tu2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tu3: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tu4: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vulmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vulmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
