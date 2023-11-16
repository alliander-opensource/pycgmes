# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class LoadStatic(IdentifiedObject):
    """
    General static load. This model represents the sensitivity of the real and reactive power consumed by the load to
      the amplitude and frequency of the bus voltage.

    LoadAggregate: Aggregate load to which this aggregate static load belongs.
    staticLoadModelType: Type of static load model.  Typical value = constantZ.
    kp1: First term voltage coefficient for active power (Kp1).  Not used when .staticLoadModelType = constantZ.
    kp2: Second term voltage coefficient for active power (Kp2).  Not used when .staticLoadModelType = constantZ.
    kp3: Third term voltage coefficient for active power (Kp3).  Not used when .staticLoadModelType = constantZ.
    kp4: Frequency coefficient for active power (Kp4)  (not = 0 if .staticLoadModelType = zIP2).  Used only when
      .staticLoadModelType = zIP2.
    ep1: First term voltage exponent for active power (Ep1).  Used only when .staticLoadModelType = exponential.
    ep2: Second term voltage exponent for active power (Ep2).  Used only when .staticLoadModelType = exponential.
    ep3: Third term voltage exponent for active power (Ep3).  Used only when .staticLoadModelType = exponential.
    kpf: Frequency deviation coefficient for active power (Kpf).  Not used when .staticLoadModelType = constantZ.
    kq1: First term voltage coefficient for reactive power (Kq1).  Not used when .staticLoadModelType = constantZ.
    kq2: Second term voltage coefficient for reactive power (Kq2).  Not used when .staticLoadModelType = constantZ.
    kq3: Third term voltage coefficient for reactive power (Kq3).  Not used when .staticLoadModelType = constantZ.
    kq4: Frequency coefficient for reactive power (Kq4)  (not = 0 when .staticLoadModelType = zIP2).  Used only when
      .staticLoadModelType - zIP2.
    eq1: First term voltage exponent for reactive power (Eq1).  Used only when .staticLoadModelType = exponential.
    eq2: Second term voltage exponent for reactive power (Eq2).  Used only when .staticLoadModelType = exponential.
    eq3: Third term voltage exponent for reactive power (Eq3).  Used only when .staticLoadModelType = exponential.
    kqf: Frequency deviation coefficient for reactive power (Kqf).  Not used when .staticLoadModelType = constantZ.
    """

    LoadAggregate: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    staticLoadModelType: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    kp1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kp2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kp3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kp4: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ep1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ep2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ep3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kpf: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kq1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kq2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kq3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kq4: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    eq1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    eq2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    eq3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kqf: float = Field(
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
