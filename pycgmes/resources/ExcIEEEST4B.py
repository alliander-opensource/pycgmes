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
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcIEEEST4B(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type ST4B model. This model is a variation of the type ST3A model, with a proportional plus integral
      (PI) regulator block replacing the lag-lead regulator characteristic that is in the ST3A model. Both potential
      and compound source rectifier excitation systems are modelled.  The PI regulator blocks have non-windup limits
      that are represented. The voltage regulator of this model is typically implemented digitally. Reference: IEEE
      421.5-2005, 7.4.

    kpr: Voltage regulator proportional gain (KPR).  Typical value = 10,75.
    kir: Voltage regulator integral gain (KIR).  Typical value = 10,75.
    ta: Voltage regulator time constant (TA) (>= 0).  Typical value = 0,02.
    vrmax: Maximum voltage regulator output (VRMAX) (> 0).  Typical value = 1.
    vrmin: Minimum voltage regulator output (VRMIN) (< 0).  Typical value = -0,87.
    kpm: Voltage regulator proportional gain output (KPM).  Typical value = 1.
    kim: Voltage regulator integral gain output (KIM).  Typical value = 0.
    vmmax: Maximum inner loop output (VMMax) (> ExcIEEEST4B.vmmin).  Typical value = 99.
    vmmin: Minimum inner loop output (VMMin) (< ExcIEEEST4B.vmmax).  Typical value = -99.
    kg: Feedback gain constant of the inner loop field regulator (KG) (>= 0).  Typical value = 0.
    kp: Potential circuit gain coefficient (KP) (> 0).  Typical value = 9,3.
    thetap: Potential circuit phase angle (thetap).  Typical value = 0.
    ki: Potential circuit gain coefficient (KI) (>= 0).  Typical value = 0.
    kc: Rectifier loading factor proportional to commutating reactance (KC) (>= 0). Typical value = 0,113.
    xl: Reactance associated with potential source (XL) (>= 0).  Typical value = 0,124.
    vbmax: Maximum excitation voltage (VBMax) (> 0).  Typical value = 11,63.
    """

    kpr: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kir: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ta: int = Field(
        default=0,
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

    kpm: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kim: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vmmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vmmin: float = Field(
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

    kp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    thetap: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ki: float = Field(
        default=0.0,
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

    xl: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vbmax: float = Field(
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
