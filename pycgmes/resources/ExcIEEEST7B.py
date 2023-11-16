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
class ExcIEEEST7B(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type ST7B model. This model is representative of static potential-source excitation systems. In this
      system, the AVR consists of a PI voltage regulator. A phase lead-lag filter in series allows the introduction
      of a derivative function, typically used with brushless excitation systems. In that case, the regulator is of
      the PID type. In addition, the terminal voltage channel includes a phase lead-lag filter.  The AVR includes
      the appropriate inputs on its reference for overexcitation limiter (OEL1), underexcitation limiter (UEL),
      stator current limiter (SCL), and current compensator (DROOP). All these limitations, when they work at
      voltage reference level, keep the PSS (VS signal from PSS) in operation. However, the UEL limitation can also
      be transferred to the high value (HV) gate acting on the output signal. In addition, the output signal passes
      through a low value (LV) gate for a ceiling overexcitation limiter (OEL2). Reference: IEEE 421.5-2005, 7.7.

    kh: High-value gate feedback gain (KH) (>= 0).  Typical value = 1.
    kia: Voltage regulator integral gain (KIA) (>= 0).  Typical value = 1.
    kl: Low-value gate feedback gain (KL) (>= 0).  Typical value = 1.
    kpa: Voltage regulator proportional gain (KPA) (> 0).  Typical value = 40.
    oelin: OEL input selector (OELin).  Typical value = noOELinput.
    tb: Regulator lag time constant (TB) (>= 0).  Typical value = 1.
    tc: Regulator lead time constant (TC) (>= 0).  Typical value = 1.
    tf: Excitation control system stabilizer time constant (TF) (>= 0).  Typical value = 1.
    tg: Feedback time constant of inner loop field voltage regulator (TG) (>= 0). Typical value = 1.
    tia: Feedback time constant (TIA) (>= 0).  Typical value = 3.
    uelin: UEL input selector (UELin). Typical value = noUELinput.
    vmax: Maximum voltage reference signal (VMAX) (> 0 and > ExcIEEEST7B.vmin).  Typical value = 1,1.
    vmin: Minimum voltage reference signal (VMIN) (> 0 and < ExcIEEEST7B.vmax).  Typical value = 0,9.
    vrmax: Maximum voltage regulator output (VRMAX) (> 0).  Typical value = 5.
    vrmin: Minimum voltage regulator output (VRMIN) (< 0).  Typical value = -4,5.
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
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
