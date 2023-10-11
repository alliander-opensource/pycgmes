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

    kf2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tf2: int = Field(
        default=0,
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

    melmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    qo: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    r: float = Field(
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
