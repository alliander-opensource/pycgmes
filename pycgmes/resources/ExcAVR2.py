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
class ExcAVR2(ExcitationSystemDynamics):
    """
    Italian excitation system corresponding to IEEE (1968) type 2 model. It represents an alternator and rotating diodes
      and electromechanic voltage regulators.

    ka: AVR gain (KA).  Typical value = 500.
    vrmn: Minimum AVR output (VRMN).  Typical value = -6.
    vrmx: Maximum AVR output (VRMX).  Typical value = 7.
    ta: AVR time constant (TA) (>= 0).  Typical value = 0,02.
    tb: AVR time constant (TB) (>= 0).  Typical value = 0.
    te: Exciter time constant (TE) (>= 0).  Typical value = 1.
    e1: Field voltage value 1 (E1).  Typical value = 4,18.
    se1: Saturation factor at E1 (S[E1]).  Typical value = 0.1.
    e2: Field voltage value 2 (E2).  Typical value = 3,14.
    se2: Saturation factor at E2 (S[E2]).  Typical value = 0,03.
    kf: Rate feedback gain (KF).  Typical value = 0,12.
    tf1: Rate feedback time constant (TF1) (>= 0).  Typical value = 1.
    tf2: Rate feedback time constant (TF2) (>= 0).  Typical value = 1.
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

    kf: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tf1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tf2: int = Field(
        default=0,
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
