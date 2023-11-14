# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

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
class UnderexcLim2Simplified(UnderexcitationLimiterDynamics):
    """
    Simplified type UEL2 underexcitation limiter.  This model can be derived from UnderexcLimIEEE2.  The limit
      characteristic (look -up table) is a single straight-line, the same as UnderexcLimIEEE2 (see Figure 10.4 (p
      32), IEEE 421.5-2005 Section 10.2).

    q0: Segment Q initial point (Q0).  Typical value = -0,31.
    q1: Segment Q end point (Q1).  Typical value = -0,1.
    p0: Segment P initial point (P0).  Typical value = 0.
    p1: Segment P end point (P1).  Typical value = 1.
    kui: Gain Under excitation limiter (KUI).  Typical value = 0,1.
    vuimin: Minimum error signal (VUIMIN) (< UnderexcLim2Simplified.vuimax).  Typical value = 0.
    vuimax: Maximum error signal (VUIMAX) (> UnderexcLim2Simplified.vuimin).  Typical value = 1.
    """

    q0: float = Field(
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

    p0: float = Field(
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

    kui: float = Field(
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

    vuimax: float = Field(
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
