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
class ExcST1A(ExcitationSystemDynamics):
    """
    Modification of an old IEEE ST1A static excitation system without overexcitation limiter (OEL) and underexcitation
      limiter (UEL).

    vimax: Maximum voltage regulator input limit (Vimax) (> 0).  Typical value = 999.
    vimin: Minimum voltage regulator input limit (Vimin) (< 0).  Typical value = -999.
    tc: Voltage regulator time constant (Tc) (>= 0).  Typical value = 1.
    tb: Voltage regulator time constant (Tb) (>= 0).  Typical value = 10.
    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 190.
    ta: Voltage regulator time constant (Ta) (>= 0).  Typical value = 0,02.
    vrmax: Maximum voltage regulator outputs (Vrmax) (> 0) .  Typical value = 7,8.
    vrmin: Minimum voltage regulator outputs (Vrmin) (< 0).  Typical value = -6,7.
    kc: Rectifier loading factor proportional to commutating reactance (Kc) (>= 0). Typical value = 0,05.
    kf: Excitation control system stabilizer gains (Kf) (>= 0).  Typical value = 0.
    tf: Excitation control system stabilizer time constant (Tf) (>= 0).  Typical value = 1.
    tc1: Voltage regulator time constant (Tc1) (>= 0).  Typical value = 0.
    tb1: Voltage regulator time constant (Tb1) (>= 0).  Typical value = 0.
    vamax: Maximum voltage regulator output (Vamax) (> 0).  Typical value = 999.
    vamin: Minimum voltage regulator output (Vamin) (< 0).  Typical value = -999.
    ilr: Exciter output current limit reference (Ilr).  Typical value = 0.
    klr: Exciter output current limiter gain (Klr).  Typical value = 0.
    xe: Excitation xfmr effective reactance (Xe).  Typical value = 0,04.
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

    tc: int = Field(
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

    kc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kf: float = Field(
        default=0.0,
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

    ilr: float = Field(
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

    xe: float = Field(
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
