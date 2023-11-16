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
from .OverexcitationLimiterDynamics import OverexcitationLimiterDynamics


@dataclass(config=DataclassConfig)
class OverexcLim2(OverexcitationLimiterDynamics):
    """
    Different from LimIEEEOEL, LimOEL2 has a fixed pickup threshold and reduces the excitation set-point by means of a
      non-windup integral regulator. Irated is the rated machine excitation current (calculated from nameplate
      conditions: Vnom, Pnom, CosPhinom).

    koi: Gain Over excitation limiter (KOI).  Typical value = 0,1.
    voimax: Maximum error signal (VOIMAX) (> OverexcLim2.voimin).  Typical value = 0.
    voimin: Minimum error signal (VOIMIN) (< OverexcLim2.voimax).  Typical value = -9999.
    ifdlim: Limit value of rated field current (IFDLIM).  Typical value = 1,05.
    """

    koi: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    voimax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    voimin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ifdlim: float = Field(
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
