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
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcIEEEST5B(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type ST5B model. The type ST5B excitation system is a variation of the type ST1A model, with
      alternative overexcitation and underexcitation inputs and additional limits. The block diagram in the IEEE
      421.5 standard has input signal Vc and does not indicate the summation point with Vref. The implementation of
      the ExcIEEEST5B shall consider summation point with Vref. Reference: IEEE 421.5-2005, 7.5.

    kr: Regulator gain (KR) (> 0).  Typical value = 200.
    t1: Firing circuit time constant (T1) (>= 0).  Typical value = 0,004.
    kc: Rectifier regulation factor (KC) (>= 0).  Typical value = 0,004.
    vrmax: Maximum voltage regulator output (VRMAX) (> 0).  Typical value = 5.
    vrmin: Minimum voltage regulator output (VRMIN) (< 0).  Typical value = -4.
    tc1: Regulator lead time constant (TC1) (>= 0).  Typical value = 0,8.
    tb1: Regulator lag time constant (TB1) (>= 0).  Typical value = 6.
    tc2: Regulator lead time constant (TC2) (>= 0).  Typical value = 0,08.
    tb2: Regulator lag time constant (TB2) (>= 0).  Typical value = 0,01.
    toc1: OEL lead time constant (TOC1) (>= 0).  Typical value = 0,1.
    tob1: OEL lag time constant (TOB1) (>= 0).  Typical value = 2.
    toc2: OEL lead time constant (TOC2) (>= 0).  Typical value = 0,08.
    tob2: OEL lag time constant (TOB2) (>= 0).  Typical value = 0,08.
    tuc1: UEL lead time constant (TUC1) (>= 0).  Typical value = 2.
    tub1: UEL lag time constant (TUB1) (>= 0).  Typical value = 10.
    tuc2: UEL lead time constant (TUC2) (>= 0).  Typical value = 0,1.
    tub2: UEL lag time constant (TUB2) (>= 0).  Typical value = 0,05.
    """

    kr: float = Field(
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

    kc: float = Field(
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

    tc1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tb1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tc2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tb2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    toc1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tob1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    toc2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tob2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tuc1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tub1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tuc2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tub2: int = Field(
        default=0,
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
