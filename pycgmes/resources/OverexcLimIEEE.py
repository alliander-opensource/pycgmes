# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .OverexcitationLimiterDynamics import OverexcitationLimiterDynamics


@dataclass(config=DataclassConfig)
class OverexcLimIEEE(OverexcitationLimiterDynamics):
    """
    The over excitation limiter model is intended to represent the significant features of OELs necessary for some
      large-scale system studies. It is the result of a pragmatic approach to obtain a model that can be widely
      applied with attainable data from generator owners. An attempt to include all variations in the functionality
      of OELs and duplicate how they interact with the rest of the excitation systems would likely result in a level
      of application insufficient for the studies for which they are intended. Reference: IEEE OEL 421.5-2005, 9.

    itfpu: OEL timed field current limiter pickup level (ITFPU).  Typical value = 1,05.
    ifdmax: OEL instantaneous field current limit (IFDMAX).  Typical value = 1,5.
    ifdlim: OEL timed field current limit (IFDLIM).  Typical value = 1,05.
    hyst: OEL pickup/drop-out hysteresis (HYST).  Typical value = 0,03.
    kcd: OEL cooldown gain (KCD).  Typical value = 1.
    kramp: OEL ramped limit rate (KRAMP).  Unit = PU / s.  Typical value = 10.
    """

    itfpu: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ifdmax: float = Field(
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

    hyst: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kcd: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kramp: float = Field(
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
