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
class ExcIEEEST1A(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type ST1A model. This model represents systems in which excitation power is supplied through a
      transformer from the generator terminals (or the unit's auxiliary bus) and is regulated by a controlled
      rectifier.  The maximum exciter voltage available from such systems is directly related to the generator
      terminal voltage. Reference: IEEE 421.5-2005, 7.1.

    ilr: Exciter output current limit reference (ILR).  Typical value = 0.
    ka: Voltage regulator gain (KA) (> 0).  Typical value = 190.
    kc: Rectifier loading factor proportional to commutating reactance (KC) (>= 0). Typical value = 0,08.
    kf: Excitation control system stabilizer gains (KF) (>= 0).  Typical value = 0.
    klr: Exciter output current limiter gain (KLR).  Typical value = 0.
    pssin: Selector of the Power System Stabilizer (PSS) input (PSSin). true = PSS input (Vs) added to error signal
      false = PSS input (Vs) added to voltage regulator output. Typical value = true.
    ta: Voltage regulator time constant (TA) (>= 0).  Typical value = 0.
    tb: Voltage regulator time constant (TB) (>= 0).  Typical value = 10.
    tb1: Voltage regulator time constant (TB1) (>= 0).  Typical value = 0.
    tc: Voltage regulator time constant (TC) (>= 0).  Typical value = 1.
    tc1: Voltage regulator time constant (TC1) (>= 0).  Typical value = 0.
    tf: Excitation control system stabilizer time constant (TF) (>= 0).  Typical value = 1.
    uelin: Selector of the connection of the UEL input (UELin).  Typical value = ignoreUELsignal.
    vamax: Maximum voltage regulator output (VAMAX) (> 0).  Typical value = 14,5.
    vamin: Minimum voltage regulator output (VAMIN) (< 0).  Typical value = -14,5.
    vimax: Maximum voltage regulator input limit (VIMAX) (> 0).  Typical value = 999.
    vimin: Minimum voltage regulator input limit (VIMIN) (< 0).  Typical value = -999.
    vrmax: Maximum voltage regulator outputs (VRMAX) (> 0).  Typical value = 7,8.
    vrmin: Minimum voltage regulator outputs (VRMIN) (< 0).  Typical value = -6,7.
    """

    ilr: float = Field(
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

    klr: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pssin: bool = Field(
        default=False,
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

    tb1: int = Field(
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

    tc1: int = Field(
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

    uelin: Optional[str] = Field(
        default=None,
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
