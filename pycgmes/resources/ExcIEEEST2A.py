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
class ExcIEEEST2A(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type ST2A model. Some static systems use both current and voltage sources (generator terminal
      quantities) to comprise the power source.  The regulator controls the exciter output through controlled
      saturation of the power transformer components.  These compound-source rectifier excitation systems are
      designated type ST2A and are represented by ExcIEEEST2A. Reference: IEEE 421.5-2005, 7.2.

    ka: Voltage regulator gain (KA) (> 0).  Typical value = 120.
    ta: Voltage regulator time constant (TA) (> 0).  Typical value = 0,15.
    vrmax: Maximum voltage regulator outputs (VRMAX) (> 0).  Typical value = 1.
    vrmin: Minimum voltage regulator outputs (VRMIN) (<= 0).  Typical value = 0.
    ke: Exciter constant related to self-excited field (KE).  Typical value = 1.
    te: Exciter time constant, integration rate associated with exciter control (TE) (> 0).  Typical value = 0,5.
    kf: Excitation control system stabilizer gains (KF) (>= 0).  Typical value = 0,05.
    tf: Excitation control system stabilizer time constant (TF) (>= 0).  Typical value = 1.
    kp: Potential circuit gain coefficient (KP) (>= 0).  Typical value = 4,88.
    ki: Potential circuit gain coefficient (KI) (>= 0).  Typical value = 8.
    kc: Rectifier loading factor proportional to commutating reactance (KC) (>= 0). Typical value = 1,82.
    efdmax: Maximum field voltage (EFDMax) (>= 0).  Typical value = 99.
    uelin: UEL input (UELin). true = HV gate false = add to error signal. Typical value = true.
    """

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

    ke: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    te: int = Field(
        default=0,
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

    kp: float = Field(
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

    efdmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    uelin: bool = Field(
        default=False,
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
