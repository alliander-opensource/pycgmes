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
class Pss5(PowerSystemStabilizerDynamics):
    """
    Detailed Italian PSS.

    kpe: Electric power input gain (KPE).  Typical value = 0,3.
    kf: Frequency/shaft speed input gain (KF).  Typical value = 5.
    isfreq: Selector for frequency/shaft speed input (isFreq). true = speed (same meaning as InputSignaKind.rotorSpeed)
      false = frequency (same meaning as InputSignalKind.busFrequency). Typical value = true (same meaning
      as InputSignalKind.rotorSpeed).
    kpss: PSS gain (KPSS).  Typical value = 1.
    ctw2: Selector for second washout enabling (CTW2). true = second washout filter is bypassed false = second washout
      filter in use. Typical value = true.
    tw1: First washout (TW1) (>= 0).  Typical value = 3,5.
    tw2: Second washout (TW2) (>= 0).  Typical value = 0.
    tl1: Lead/lag time constant (TL1) (>= 0).  Typical value = 0.
    tl2: Lead/lag time constant (TL2) (>= 0).  If = 0, both blocks are bypassed.  Typical value = 0.
    tl3: Lead/lag time constant (TL3) (>= 0).  Typical value = 0.
    tl4: Lead/lag time constant (TL4) (>= 0).  If = 0, both blocks are bypassed.  Typical value = 0.
    vsmn: Stabilizer output maximum limit (VSMN).  Typical value = -0,1.
    vsmx: Stabilizer output minimum limit (VSMX).  Typical value = 0,1.
    tpe: Electric power filter time constant (TPE) (>= 0).  Typical value = 0,05.
    pmin: Minimum power PSS enabling (Pmin).  Typical value = 0,25.
    deadband: Stabilizer output deadband (DEADBAND).  Typical value = 0.
    vadat: Signal selector (VadAtt). true = closed (generator power is greater than Pmin) false = open (Pe is smaller
      than Pmin). Typical value = true.
    """

    kpe: float = Field(
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

    isfreq: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    kpss: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ctw2: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    tw1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tw2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tl1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tl2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tl3: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tl4: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vsmn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vsmx: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tpe: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    pmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    deadband: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vadat: bool = Field(
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
