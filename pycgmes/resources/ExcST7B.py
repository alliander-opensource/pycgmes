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
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcST7B(ExcitationSystemDynamics):
    """
    Modified IEEE ST7B static excitation system without stator current limiter (SCL) and current compensator (DROOP)
      inputs.

    kh: High-value gate feedback gain (Kh) (>= 0).  Typical value = 1.
    kia: Voltage regulator integral gain (Kia) (>= 0).  Typical value = 1.
    kl: Low-value gate feedback gain (Kl) (>= 0).  Typical value = 1.
    kpa: Voltage regulator proportional gain (Kpa) (> 0).  Typical value = 40.
    oelin: OEL input selector (OELin). Typical value = noOELinput.
    tb: Regulator lag time constant (Tb) (>= 0).  Typical value = 1.
    tc: Regulator lead time constant (Tc) (>= 0).  Typical value = 1.
    tf: Excitation control system stabilizer time constant (Tf) (>= 0).  Typical value = 1.
    tg: Feedback time constant of inner loop field voltage regulator (Tg) (>= 0).  Typical value = 1.
    tia: Feedback time constant (Tia) (>= 0).  Typical value = 3.
    ts: Rectifier firing time constant (Ts) (>= 0).  Typical value = 0.
    uelin: UEL input selector (UELin). Typical value = noUELinput.
    vmax: Maximum voltage reference signal (Vmax) (> 0 and > ExcST7B.vmin)).  Typical value = 1,1.
    vmin: Minimum voltage reference signal (Vmin) (> 0 and < ExcST7B.vmax).  Typical value = 0,9.
    vrmax: Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 5.
    vrmin: Minimum voltage regulator output (Vrmin) (< 0).  Typical value = -4,5.
    """

    kh: float = Field(
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

    kl: float = Field(
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

    tf: int = Field(
        default=0,
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

    tia: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ts: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    uelin: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    vmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vmin: float = Field(
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
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
