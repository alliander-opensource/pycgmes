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

from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass(config=DataclassConfig)
class PssSK(PowerSystemStabilizerDynamics):
    """
    Slovakian PSS with three inputs.

    k1: Gain P (K1).  Typical value = -0,3.
    k2: Gain fE (K2).  Typical value = -0,15.
    k3: Gain If (K3).  Typical value = 10.
    t1: Denominator time constant (T1) (> 0,005).  Typical value = 0,3.
    t2: Filter time constant (T2) (> 0,005).  Typical value = 0,35.
    t3: Denominator time constant (T3) (> 0,005).  Typical value = 0,22.
    t4: Filter time constant (T4) (> 0,005).  Typical value = 0,02.
    t5: Denominator time constant (T5) (> 0,005).  Typical value = 0,02.
    t6: Filter time constant (T6) (> 0,005).  Typical value = 0,02.
    vsmax: Stabilizer output maximum limit (VSMAX) (> PssSK.vsmin).  Typical value = 0,4.
    vsmin: Stabilizer output minimum limit (VSMIN) (< PssSK.vsmax).  Typical value = -0.4.
    """

    k1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k3: float = Field(
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

    t5: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t6: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vsmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vsmin: float = Field(
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
