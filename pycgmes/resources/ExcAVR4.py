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
class ExcAVR4(ExcitationSystemDynamics):
    """
    Italian excitation system. It represents a static exciter and electric voltage regulator.

    ka: AVR gain (KA).  Typical value = 300.
    vrmn: Minimum AVR output (VRMN).  Typical value = 0.
    vrmx: Maximum AVR output (VRMX).  Typical value = 5.
    t1: AVR time constant (T1) (>= 0).  Typical value = 4,8.
    t2: AVR time constant (T2) (>= 0).  Typical value = 1,5.
    t3: AVR time constant (T3) (>= 0).  Typical value = 0.
    t4: AVR time constant (T4) (>= 0).  Typical value = 0.
    ke: Exciter gain (KE).  Typical value = 1.
    vfmx: Maximum exciter output (VFMX).  Typical value = 5.
    vfmn: Minimum exciter output (VFMN).  Typical value = 0.
    kif: Exciter internal reactance (KIF).  Typical value = 0.
    tif: Exciter current feedback time constant (TIF) (>= 0).  Typical value = 0.
    t1if: Exciter current feedback time constant (T1IF) (>= 0).  Typical value = 60.
    imul: AVR output voltage dependency selector (IMUL). true = selector is connected false = selector is not connected.
      Typical value = true.
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

    ke: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vfmx: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vfmn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kif: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tif: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t1if: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    imul: bool = Field(
        default=False,
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
