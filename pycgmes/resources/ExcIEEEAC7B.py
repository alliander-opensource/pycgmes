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
class ExcIEEEAC7B(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type AC7B model. The model represents excitation systems which consist of an AC alternator with
      either stationary or rotating rectifiers to produce the DC field requirements. It is an upgrade to earlier AC
      excitation systems, which replace only the controls but retain the AC alternator and diode rectifier bridge.
      Reference: IEEE 421.5-2005, 6.7. Note, however, that in IEEE 421.5-2005, the [1 / sTE] block is shown as [1 /
      (1 + sTE)], which is incorrect.

    kpr: Voltage regulator proportional gain (KPR) (> 0 if ExcIEEEAC7B.kir = 0).  Typical value = 4,24.
    kir: Voltage regulator integral gain (KIR) (>= 0).  Typical value = 4,24.
    kdr: Voltage regulator derivative gain (KDR) (>= 0).  Typical value = 0.
    tdr: Lag time constant (TDR) (>= 0).  Typical value = 0.
    vrmax: Maximum voltage regulator output (VRMAX) (> 0).  Typical value = 5,79.
    vrmin: Minimum voltage regulator output (VRMIN) (< 0).  Typical value = -5,79.
    kpa: Voltage regulator proportional gain (KPA) (> 0 if ExcIEEEAC7B.kia = 0).  Typical value = 65,36.
    kia: Voltage regulator integral gain (KIA) (>= 0).  Typical value = 59,69.
    vamax: Maximum voltage regulator output (VAMAX) (> 0).  Typical value = 1.
    vamin: Minimum voltage regulator output (VAMIN) (< 0).  Typical value = -0,95.
    kp: Potential circuit gain coefficient (KP) (> 0).  Typical value = 4,96.
    kl: Exciter field voltage lower limit parameter (KL).  Typical value = 10.
    te: Exciter time constant, integration rate associated with exciter control (TE) (> 0).  Typical value = 1,1.
    vfemax: Exciter field current limit reference (VFEMAX).  Typical value = 6,9.
    vemin: Minimum exciter voltage output (VEMIN) (<= 0).  Typical value = 0.
    ke: Exciter constant related to self-excited field (KE).  Typical value = 1.
    kc: Rectifier loading factor proportional to commutating reactance (KC) (>= 0). Typical value = 0,18.
    kd: Demagnetizing factor, a function of exciter alternator reactances (KD) (>= 0).  Typical value = 0,02.
    kf1: Excitation control system stabilizer gain (KF1) (>= 0).  Typical value = 0,212.
    kf2: Excitation control system stabilizer gain (KF2) (>= 0).  Typical value = 0.
    kf3: Excitation control system stabilizer gain (KF3) (>= 0).  Typical value = 0.
    tf: Excitation control system stabilizer time constant (TF) (> 0).  Typical value = 1.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (VE1) (> 0).
      Typical value = 6,3.
    seve1: Exciter saturation function value at the corresponding exciter voltage, VE1, back of commutating reactance
      (SE[VE1]) (>= 0).  Typical value = 0,44.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (VE2) (> 0).
      Typical value = 3,02.
    seve2: Exciter saturation function value at the corresponding exciter voltage, VE2, back of commutating reactance
      (SE[VE2]) (>= 0).  Typical value = 0,075.
    """

    kpr: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kir: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kdr: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tdr: int = Field(
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

    kpa: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kia: float = Field(
        default=0.0,
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

    kp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kl: float = Field(
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

    vfemax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vemin: float = Field(
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

    kf3: float = Field(
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

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
