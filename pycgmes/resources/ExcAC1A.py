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
class ExcAC1A(ExcitationSystemDynamics):
    """
    Modified IEEE AC1A alternator-supplied rectifier excitation system with different rate feedback source.

    tb: Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.
    tc: Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.
    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 400.
    ta: Voltage regulator time constant (Ta) (> 0).  Typical value = 0,02.
    vamax: Maximum voltage regulator output (Vamax) (> 0).  Typical value = 14,5.
    vamin: Minimum voltage regulator output (Vamin) (< 0).  Typical value = -14,5.
    te: Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 0,8.
    kf: Excitation control system stabilizer gains (Kf) (>= 0).  Typical value = 0,03.
    kf1: Coefficient to allow different usage of the model (Kf1) (>= 0).  Typical value = 0.
    kf2: Coefficient to allow different usage of the model (Kf2) (>= 0).  Typical value = 1.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks) (>= 0).  Typical value = 0.
    tf: Excitation control system stabilizer time constant (Tf) (> 0).  Typical value = 1.
    kc: Rectifier loading factor proportional to commutating reactance (Kc) (>= 0). Typical value = 0,2.
    kd: Demagnetizing factor, a function of exciter alternator reactances (Kd) (>= 0).  Typical value = 0,38.
    ke: Exciter constant related to self-excited field (Ke).  Typical value = 1.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1) (> 0).
      Typical value = 4,18.
    seve1: Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance
      (Se[Ve1]) (>= 0).  Typical value = 0,1.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2) (> 0).
      Typical value = 3,14.
    seve2: Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance
      (Se[Ve2]) (>= 0).  Typical value = 0,03.
    vrmax: Maximum voltage regulator outputs (Vrmax) (> 0).  Typical value = 6,03.
    vrmin: Minimum voltage regulator outputs (Vrmin) (< 0).  Typical value = -5,43.
    hvlvgates: Indicates if both HV gate and LV gate are active (HVLVgates). true = gates are used false = gates are not
      used. Typical value = true.
    """

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

    vamax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vamin: float = Field(
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

    kf1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kf2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ks: float = Field(
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

    kc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kd: float = Field(
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

    ve1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    seve1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ve2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    seve2: float = Field(
        default=0.0,
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

    hvlvgates: bool = Field(
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
