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
class UnderexcLimIEEE2(UnderexcitationLimiterDynamics):
    """
    Type UEL2 underexcitation limiter which has either a straight-line or multi-segment characteristic when plotted in
      terms of machine reactive power output vs. real power output. Reference: IEEE UEL2 421.5-2005, 10.2  (limit
      characteristic lookup table shown in Figure 10.4 (p 32)).

    tuv: Voltage filter time constant (TUV) (>= 0).  Typical value = 5.
    tup: Real power filter time constant (TUP) (>= 0).  Typical value = 5.
    tuq: Reactive power filter time constant (TUQ) (>= 0).  Typical value = 0.
    kui: UEL integral gain (KUI).  Typical value = 0,5.
    kul: UEL proportional gain (KUL).  Typical value = 0,8.
    vuimax: UEL integrator output maximum limit (VUIMAX) (> UnderexcLimIEEE2.vuimin).  Typical value = 0,25.
    vuimin: UEL integrator output minimum limit (VUIMIN) (< UnderexcLimIEEE2.vuimax).  Typical value = 0.
    kuf: UEL excitation system stabilizer gain (KUF).  Typical value = 0.
    kfb: Gain associated with optional integrator feedback input signal to UEL (KFB).  Typical value = 0.
    tul: Time constant associated with optional integrator feedback input signal to UEL (TUL) (>= 0).  Typical value =
      0.
    tu1: UEL lead time constant (TU1) (>= 0).  Typical value = 0.
    tu2: UEL lag time constant (TU2) (>= 0).  Typical value = 0.
    tu3: UEL lead time constant (TU3) (>= 0).  Typical value = 0.
    tu4: UEL lag time constant (TU4) (>= 0).  Typical value = 0.
    vulmax: UEL output maximum limit (VULMAX) (> UnderexcLimIEEE2.vulmin).  Typical value = 0,25.
    vulmin: UEL output minimum limit (VULMIN) (< UnderexcLimIEEE2.vulmax).  Typical value = 0.
    p0: Real power values for endpoints (P0).  Typical value = 0.
    q0: Reactive power values for endpoints (Q0).  Typical value = -0,31.
    p1: Real power values for endpoints (P1).  Typical value = 0,3.
    q1: Reactive power values for endpoints (Q1).  Typical value = -0,31.
    p2: Real power values for endpoints (P2).  Typical value = 0,6.
    q2: Reactive power values for endpoints (Q2).  Typical value = -0,28.
    p3: Real power values for endpoints (P3).  Typical value = 0,9.
    q3: Reactive power values for endpoints (Q3).  Typical value = -0,21.
    p4: Real power values for endpoints (P4).  Typical value = 1,02.
    q4: Reactive power values for endpoints (Q4).  Typical value = 0.
    p5: Real power values for endpoints (P5).
    q5: Reactive power values for endpoints (Q5).
    p6: Real power values for endpoints (P6).
    q6: Reactive power values for endpoints (Q6).
    p7: Real power values for endpoints (P7).
    q7: Reactive power values for endpoints (Q7).
    p8: Real power values for endpoints (P8).
    q8: Reactive power values for endpoints (Q8).
    p9: Real power values for endpoints (P9).
    q9: Reactive power values for endpoints (Q9).
    p10: Real power values for endpoints (P10).
    q10: Reactive power values for endpoints (Q10).
    k1: UEL terminal voltage exponent applied to real power input to UEL limit look-up table (k1).  Typical value = 2.
    k2: UEL terminal voltage exponent applied to reactive power output from UEL limit look-up table (k2).  Typical value
      = 2.
    """

    tuv: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tup: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tuq: int = Field(
        default=0,
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

    kuf: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kfb: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tul: int = Field(
        default=0,
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

    p0: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    q0: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    p1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    q1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    p2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    q2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    p3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    q3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    p4: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    q4: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    p5: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    q5: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    p6: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    q6: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    p7: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    q7: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    p8: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    q8: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    p9: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    q9: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    p10: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    q10: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k2: float = Field(
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
