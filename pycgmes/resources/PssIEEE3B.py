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
class PssIEEE3B(PowerSystemStabilizerDynamics):
    """
    IEEE 421.5-2005 type PSS3B power system stabilizer model. The PSS model PSS3B has dual inputs of electrical power
      and rotor angular frequency deviation. The signals are used to derive an equivalent mechanical power signal.
      This model has 2 input signals. They have the following fixed types (expressed in terms of InputSignalKind
      values): the first one is of rotorAngleFrequencyDeviation type and the second one is of
      generatorElectricalPower type. Reference: IEEE 3B 421.5-2005, 8.3.

    t1: Transducer time constant (T1) (>= 0).  Typical value = 0,012.
    t2: Transducer time constant (T2) (>= 0).  Typical value = 0,012.
    tw1: Washout time constant (Tw1) (>= 0).  Typical value = 0,3.
    tw2: Washout time constant (Tw2) (>= 0).  Typical value = 0,3.
    tw3: Washout time constant (Tw3) (>= 0).  Typical value = 0,6.
    ks1: Gain on signal # 1 (Ks1).  Typical value = -0,602.
    ks2: Gain on signal # 2 (Ks2).  Typical value = 30,12.
    a1: Notch filter parameter (A1).  Typical value = 0,359.
    a2: Notch filter parameter (A2).  Typical value = 0,586.
    a3: Notch filter parameter (A3).  Typical value = 0,429.
    a4: Notch filter parameter (A4).  Typical value = 0,564.
    a5: Notch filter parameter (A5).  Typical value = 0,001.
    a6: Notch filter parameter (A6).  Typical value = 0.
    a7: Notch filter parameter (A7).  Typical value = 0,031.
    a8: Notch filter parameter (A8).  Typical value = 0.
    vstmax: Stabilizer output maximum limit (Vstmax) (> PssIEEE3B.vstmin).  Typical value = 0,1.
    vstmin: Stabilizer output minimum limit (Vstmin) (< PssIEEE3B.vstmax).  Typical value = -0,1.
    """

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

    tw3: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ks1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ks2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    a1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    a2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    a3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    a4: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    a5: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    a6: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    a7: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    a8: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vstmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vstmin: float = Field(
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
