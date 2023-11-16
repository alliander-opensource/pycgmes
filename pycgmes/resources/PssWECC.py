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

from ..utils.profile import BaseProfile, Profile
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass
class PssWECC(PowerSystemStabilizerDynamics):
    """
    Dual input power system stabilizer, based on IEEE type 2, with modified output limiter defined by WECC (Western
      Electricity Coordinating Council, USA).

    inputSignal1Type: Type of input signal #1 (rotorAngularFrequencyDeviation, busFrequencyDeviation,
      generatorElectricalPower, generatorAcceleratingPower, busVoltage, or busVoltageDerivative -
      shall be different than PssWECC.inputSignal2Type).  Typical value =
      rotorAngularFrequencyDeviation.
    inputSignal2Type: Type of input signal #2 (rotorAngularFrequencyDeviation, busFrequencyDeviation,
      generatorElectricalPower, generatorAcceleratingPower, busVoltage, busVoltageDerivative -
      shall be different than PssWECC.inputSignal1Type).  Typical value = busVoltageDerivative.
    k1: Input signal 1 gain (K1).  Typical value = 1,13.
    t1: Input signal 1 transducer time constant (T1) (>= 0).  Typical value = 0,037.
    k2: Input signal 2 gain (K2).  Typical value = 0,0.
    t2: Input signal 2 transducer time constant (T2) (>= 0).  Typical value = 0,0.
    t3: Stabilizer washout time constant (T3) (>= 0).  Typical value = 9,5.
    t4: Stabilizer washout time lag constant (T4) (>= 0).  Typical value = 9,5.
    t5: Lead time constant (T5) (>= 0).  Typical value = 1,7.
    t6: Lag time constant (T6) (>= 0).  Typical value = 1,5.
    t7: Lead time constant (T7) (>= 0).  Typical value = 1,7.
    t8: Lag time constant (T8) (>= 0).  Typical value = 1,5.
    t10: Lag time constant (T10) (>= 0).  Typical value = 0.
    t9: Lead time constant (T9) (>= 0).  Typical value = 0.
    vsmax: Maximum output signal (Vsmax) (> PssWECC.vsmin). Typical value = 0,05.
    vsmin: Minimum output signal (Vsmin) (< PssWECC.vsmax).  Typical value = -0,05.
    vcu: Maximum value for voltage compensator output (VCU). Typical value = 0.
    vcl: Minimum value for voltage compensator output (VCL). Typical value = 0.
    """

    inputSignal1Type: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    inputSignal2Type: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    k1: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t1: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    k2: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t2: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t3: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t4: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t5: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t6: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t7: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t8: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t10: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    t9: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    vsmax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    vsmin: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    vcu: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    vcl: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
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
