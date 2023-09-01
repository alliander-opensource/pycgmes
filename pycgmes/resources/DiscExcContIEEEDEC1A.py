"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics


@dataclass(config=DataclassConfig)
class DiscExcContIEEEDEC1A(DiscontinuousExcitationControlDynamics):
    """
    IEEE type DEC1A discontinuous excitation control model that boosts generator excitation to a level higher than that
      demanded by the voltage regulator and stabilizer immediately following a system fault. Reference: IEEE
      421.5-2005, 12.2.

    vtlmt: Voltage reference (VTLMT).  Typical value = 1,1.
    vomax: Limiter (VOMAX) (> DiscExcContIEEEDEC1A.vomin).  Typical value = 0,3.
    vomin: Limiter (VOMIN) (< DiscExcContIEEEDEC1A.vomax).  Typical value = 0,1.
    ketl: Terminal voltage limiter gain (KETL).  Typical value = 47.
    vtc: Terminal voltage level reference (VTC).  Typical value = 0,95.
    val: Regulator voltage reference (VAL).  Typical value = 5,5.
    esc: Speed change reference (ESC).  Typical value = 0,0015.
    kan: Discontinuous controller gain (KAN).  Typical value = 400.
    tan: Discontinuous controller time constant (TAN) (>= 0).  Typical value = 0,08.
    tw5: DEC washout time constant (TW5) (>= 0).  Typical value = 5.
    vsmax: Limiter (VSMAX)(> DiscExcContIEEEDEC1A.vsmin).  Typical value = 0,2.
    vsmin: Limiter (VSMIN) (< DiscExcContIEEEDEC1A.vsmax).  Typical value = -0,066.
    td: Time constant (TD) (>= 0).  Typical value = 0,03.
    tl1: Time constant (TL1) (>= 0).  Typical value = 0,025.
    tl2: Time constant (TL2) (>= 0).  Typical value = 1,25.
    vtm: Voltage limits (VTM).  Typical value = 1,13.
    vtn: Voltage limits (VTN).  Typical value = 1,12.
    vanmax: Limiter for Van (VANMAX).
    """

    vtlmt: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vomax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vomin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ketl: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vtc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    val: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    esc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kan: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tan: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tw5: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vsmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vsmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    td: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tl1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tl2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vtm: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vtn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vanmax: float = Field(
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
