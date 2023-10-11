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
class ExcST6B(ExcitationSystemDynamics):
    """
    Modified IEEE ST6B static excitation system with PID controller and optional inner feedback loop.

    ilr: Exciter output current limit reference (Ilr) (> 0).  Typical value = 4,164.
    k1: Selector (K1). true = feedback is from Ifd false = feedback is not from Ifd. Typical value = true.
    kcl: Exciter output current limit adjustment (Kcl) (> 0).  Typical value = 1,0577.
    kff: Pre-control gain constant of the inner loop field regulator (Kff).  Typical value = 1.
    kg: Feedback gain constant of the inner loop field regulator (Kg) (>= 0).  Typical value = 1.
    kia: Voltage regulator integral gain (Kia) (> 0).  Typical value = 45,094.
    klr: Exciter output current limit adjustment (Kcl) (> 0).  Typical value = 17,33.
    km: Forward gain constant of the inner loop field regulator (Km).  Typical value = 1.
    kpa: Voltage regulator proportional gain (Kpa) (> 0).  Typical value = 18,038.
    kvd: Voltage regulator derivative gain (Kvd).  Typical value = 0.
    oelin: OEL input selector (OELin).  Typical value = noOELinput (corresponds to OELin = 0 on diagram).
    tg: Feedback time constant of inner loop field voltage regulator (Tg) (>= 0).  Typical value = 0,02.
    ts: Rectifier firing time constant (Ts) (>= 0).  Typical value = 0.
    tvd: Voltage regulator derivative gain (Tvd) (>= 0).  Typical value = 0.
    vamax: Maximum voltage regulator output (Vamax) (> 0).  Typical value = 4,81.
    vamin: Minimum voltage regulator output (Vamin) (< 0).  Typical value = -3,85.
    vilim: Selector (Vilim). true = Vimin-Vimax limiter is active false = Vimin-Vimax limiter is not active. Typical
      value = true.
    vimax: Maximum voltage regulator input limit (Vimax) (> ExcST6B.vimin).  Typical value = 10.
    vimin: Minimum voltage regulator input limit (Vimin) (< ExcST6B.vimax).  Typical value = -10.
    vmult: Selector (vmult). true = multiply regulator output by terminal voltage false = do not multiply regulator
      output by terminal voltage.  Typical value = true.
    vrmax: Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 4,81.
    vrmin: Minimum voltage regulator output (Vrmin) (< 0).  Typical value = -3,85.
    xc: Excitation source reactance (Xc).  Typical value = 0,05.
    """

    ilr: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k1: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    kcl: float = Field(
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

    kvd: float = Field(
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

    ts: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tvd: int = Field(
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

    vilim: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

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

    vmult: bool = Field(
        default=False,
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

    xc: float = Field(
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
