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
class ExcIEEEST3A(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type ST3A model.  Some static systems utilize a field voltage control loop to linearize the exciter
      control characteristic. This also makes the output independent of supply source variations until supply
      limitations are reached.  These systems utilize a variety of controlled-rectifier designs: full thyristor
      complements or hybrid bridges in either series or shunt configurations. The power source can consist of only a
      potential source, either fed from the machine terminals or from internal windings. Some designs can have
      compound power sources utilizing both machine potential and current. These power sources are represented as
      phasor combinations of machine terminal current and voltage and are accommodated by suitable parameters in
      model type ST3A which is represented by ExcIEEEST3A. Reference: IEEE 421.5-2005, 7.3.

    vimax: Maximum voltage regulator input limit (VIMAX) (> 0).  Typical value = 0,2.
    vimin: Minimum voltage regulator input limit (VIMIN) (< 0).  Typical value = -0,2.
    ka: Voltage regulator gain (KA) (> 0). This is parameter K in the IEEE standard. Typical value = 200.
    ta: Voltage regulator time constant (TA) (>= 0).  Typical value = 0.
    tb: Voltage regulator time constant (TB) (>= 0).  Typical value = 10.
    tc: Voltage regulator time constant (TC) (>= 0).  Typical value = 1.
    vrmax: Maximum voltage regulator output (VRMAX) (> 0).  Typical value = 10.
    vrmin: Minimum voltage regulator output (VRMIN) (< 0).  Typical value = -10.
    km: Forward gain constant of the inner loop field regulator (KM) (> 0).  Typical value = 7,93.
    tm: Forward time constant of inner loop field regulator (TM) (> 0).  Typical value = 0,4.
    vmmax: Maximum inner loop output (VMMax) (> 0).  Typical value = 1.
    vmmin: Minimum inner loop output (VMMin) (<= 0).  Typical value = 0.
    kg: Feedback gain constant of the inner loop field regulator (KG) (>= 0).  Typical value = 1.
    kp: Potential circuit gain coefficient (KP) (> 0).  Typical value = 6,15.
    thetap: Potential circuit phase angle (thetap).  Typical value = 0.
    ki: Potential circuit gain coefficient (KI) (>= 0).  Typical value = 0.
    kc: Rectifier loading factor proportional to commutating reactance (KC) (>= 0). Typical value = 0,2.
    xl: Reactance associated with potential source (XL) (>= 0).  Typical value = 0,081.
    vbmax: Maximum excitation voltage (VBMax) (> 0).  Typical value = 6,9.
    vgmax: Maximum inner loop feedback voltage (VGMax) (>= 0).  Typical value = 5,8.
    """

    vimax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vimin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ka: float = Field(
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

    tb: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tc: int = Field(
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

    vgmax: float = Field(
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
