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
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcIEEEST6B(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type ST6B model. This model consists of a PI voltage regulator with an inner loop field voltage
      regulator and pre-control. The field voltage regulator implements a proportional control. The pre-control and
      the delay in the feedback circuit increase the dynamic response. Reference: IEEE 421.5-2005, 7.6.

    ilr: Exciter output current limit reference (ILR) (> 0).  Typical value = 4,164.
    kci: Exciter output current limit adjustment (KCI) (> 0).  Typical value = 1,0577.
    kff: Pre-control gain constant of the inner loop field regulator (KFF). Typical value = 1.
    kg: Feedback gain constant of the inner loop field regulator (KG) (>= 0).  Typical value = 1.
    kia: Voltage regulator integral gain (KIA) (> 0).  Typical value = 45,094.
    klr: Exciter output current limiter gain (KLR) (> 0).  Typical value = 17,33.
    km: Forward gain constant of the inner loop field regulator (KM).  Typical value = 1.
    kpa: Voltage regulator proportional gain (KPA) (> 0).  Typical value = 18,038.
    oelin: OEL input selector (OELin). Typical value = noOELinput.
    tg: Feedback time constant of inner loop field voltage regulator (TG) (>= 0). Typical value = 0,02.
    vamax: Maximum voltage regulator output (VAMAX) (> 0).  Typical value = 4,81.
    vamin: Minimum voltage regulator output (VAMIN) (< 0).  Typical value = -3,85.
    vrmax: Maximum voltage regulator output (VRMAX) (> 0).  Typical value = 4,81.
    vrmin: Minimum voltage regulator output (VRMIN) (< 0).  Typical value = -3,85.
    """

    ilr: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kci: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kff: float = Field(
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

    kia: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    klr: float = Field(
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

    kpa: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    oelin: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    tg: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vamax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vamin: float = Field(
        default=0.0,
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

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
