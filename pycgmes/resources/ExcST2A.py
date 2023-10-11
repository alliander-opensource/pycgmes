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
class ExcST2A(ExcitationSystemDynamics):
    """
    Modified IEEE ST2A static excitation system with another lead-lag block added to match the model defined by WECC.

    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 120.
    ta: Voltage regulator time constant (Ta) (> 0).  Typical value = 0,15.
    vrmax: Maximum voltage regulator outputs (Vrmax) (> 0).  Typical value = 1.
    vrmin: Minimum voltage regulator outputs (Vrmin) (< 0).  Typical value = -1.
    ke: Exciter constant related to self-excited field (Ke).  Typical value = 1.
    te: Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 0,5.
    kf: Excitation control system stabilizer gains (kf) (>= 0).  Typical value = 0,05.
    tf: Excitation control system stabilizer time constant (Tf) (>= 0).  Typical value = 0,7.
    kp: Potential circuit gain coefficient (Kp) (>= 0).  Typical value = 4,88.
    ki: Potential circuit gain coefficient (Ki) (>= 0).  Typical value = 8.
    kc: Rectifier loading factor proportional to commutating reactance (Kc) (>= 0).  Typical value = 1,82.
    efdmax: Maximum field voltage (Efdmax) (>= 0).  Typical value = 99.
    uelin: UEL input (UELin). true = HV gate false = add to error signal. Typical value = false.
    tb: Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.
    tc: Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.
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

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
