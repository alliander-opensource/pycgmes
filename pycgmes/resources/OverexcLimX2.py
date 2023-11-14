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
class OverexcLimX2(OverexcitationLimiterDynamics):
    """
    Field voltage or current overexcitation limiter designed to protect the generator field of an AC machine with
      automatic excitation control from overheating due to prolonged overexcitation.

    m: (m). true = IFD limiting false = EFD limiting.
    efdrated: Rated field voltage if m = false or rated field current if m = true (EFDRATED).  Typical value = 1,05.
    efd1: Low voltage or current point on the inverse time characteristic (EFD1).  Typical value = 1,1.
    t1: Time to trip the exciter at the low voltage or current point on the inverse time characteristic (TIME1) (>= 0).
      Typical value = 120.
    efd2: Mid voltage or current point on the inverse time characteristic (EFD2).  Typical value = 1,2.
    t2: Time to trip the exciter at the mid voltage or current point on the inverse time characteristic (TIME2) (>= 0).
      Typical value = 40.
    efd3: High voltage or current point on the inverse time characteristic (EFD3).  Typical value = 1,5.
    t3: Time to trip the exciter at the high voltage or current point on the inverse time characteristic (TIME3) (>= 0).
      Typical value = 15.
    efddes: Desired field voltage if m = false or desired field current if m = true (EFDDES).  Typical value = 1.
    kmx: Gain (KMX).  Typical value = 0,002.
    vlow: Low voltage limit (VLOW) (> 0).
    """

    m: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    efdrated: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efd1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efd2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efd3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t3: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efddes: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kmx: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vlow: float = Field(
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
