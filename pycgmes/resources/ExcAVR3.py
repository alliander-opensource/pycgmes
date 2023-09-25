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
class ExcAVR3(ExcitationSystemDynamics):
    """
    Italian excitation system. It represents an exciter dynamo and electric regulator.

    ka: AVR gain (KA).  Typical value = 100.
    vrmn: Minimum AVR output (VRMN).  Typical value = -7,5.
    vrmx: Maximum AVR output (VRMX).  Typical value = 7,5.
    t1: AVR time constant (T1) (>= 0).  Typical value = 20.
    t2: AVR time constant (T2) (>= 0).  Typical value = 1,6.
    t3: AVR time constant (T3) (>= 0).  Typical value = 0,66.
    t4: AVR time constant (T4) (>= 0).  Typical value = 0,07.
    te: Exciter time constant (TE) (>= 0).  Typical value = 1.
    e1: Field voltage value 1 (E1).  Typical value = 4,18.
    se1: Saturation factor at E1 (S[E1]).  Typical value = 0,1.
    e2: Field voltage value 2 (E2).  Typical value = 3,14.
    se2: Saturation factor at E2 (S[E2]).  Typical value = 0,03.
    """

    ka: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vrmn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vrmx: float = Field(
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

    t2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t3: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t4: int = Field(
        default=0,
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

    e1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    se1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    e2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    se2: float = Field(
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
