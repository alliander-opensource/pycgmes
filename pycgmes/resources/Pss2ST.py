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
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass(config=DataclassConfig)
class Pss2ST(PowerSystemStabilizerDynamics):
    """
    PTI microprocessor-based stabilizer type 1.

    inputSignal1Type: Type of input signal #1 (rotorAngularFrequencyDeviation, busFrequencyDeviation,
      generatorElectricalPower, generatorAcceleratingPower, busVoltage, or busVoltageDerivative -
      shall be different than Pss2ST.inputSignal2Type).  Typical value =
      rotorAngularFrequencyDeviation.
    inputSignal2Type: Type of input signal #2 (rotorAngularFrequencyDeviation, busFrequencyDeviation,
      generatorElectricalPower, generatorAcceleratingPower, busVoltage, or busVoltageDerivative -
      shall be different than Pss2ST.inputSignal1Type).  Typical value = busVoltageDerivative.
    k1: Gain (K1).
    k2: Gain (K2).
    t1: Time constant (T1) (>= 0).
    t2: Time constant (T2) (>= 0).
    t3: Time constant (T3) (>= 0).
    t4: Time constant (T4) (>= 0).
    t5: Time constant (T5) (>= 0).
    t6: Time constant (T6) (>= 0).
    t7: Time constant (T7) (>= 0).
    t8: Time constant (T8) (>= 0).
    t9: Time constant (T9) (>= 0).
    t10: Time constant (T10) (>= 0).
    lsmax: Limiter (LSMAX) (> Pss2ST.lsmin).
    lsmin: Limiter (LSMIN) (< Pss2ST.lsmax).
    vcu: Cutoff limiter (VCU).
    vcl: Cutoff limiter (VCL).
    """

    inputSignal1Type: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    inputSignal2Type: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

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

    t7: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t8: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t9: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t10: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    lsmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    lsmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vcu: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vcl: float = Field(
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
