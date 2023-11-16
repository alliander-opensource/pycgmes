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
class ExcIEEEDC4B(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type DC4B model. These excitation systems utilize a field-controlled DC commutator exciter with a
      continuously acting voltage regulator having supplies obtained from the generator or auxiliary bus. Reference:
      IEEE 421.5-2005, 5.4.

    ka: Voltage regulator gain (KA) (> 0).  Typical value = 1.
    ta: Voltage regulator time constant (TA) (> 0).  Typical value = 0,2.
    kp: Regulator proportional gain (KP) (>= 0).  Typical value = 20.
    ki: Regulator integral gain (KI) (>= 0).  Typical value = 20.
    kd: Regulator derivative gain (KD) (>= 0).  Typical value = 20.
    td: Regulator derivative filter time constant (TD) (> 0 if ExcIEEEDC4B.kd > 0).  Typical value = 0,01.
    vrmax: Maximum voltage regulator output (VRMAX) (> ExcIEEEDC4B.vrmin).  Typical value = 2,7.
    vrmin: Minimum voltage regulator output (VRMIN) (<= 0 and < ExcIEEEDC4B.vrmax).  Typical value = -0,9.
    ke: Exciter constant related to self-excited field (KE).  Typical value = 1.
    te: Exciter time constant, integration rate associated with exciter control (TE) (> 0).  Typical value = 0,8.
    kf: Excitation control system stabilizer gain (KF) (>= 0).  Typical value = 0.
    tf: Excitation control system stabilizer time constant (TF) (>= 0).  Typical value = 1.
    efd1: Exciter voltage at which exciter saturation is defined (EFD1) (> 0).  Typical value = 1,75.
    seefd1: Exciter saturation function value at the corresponding exciter voltage, EFD1 (SE[EFD1]) (>= 0).  Typical
      value = 0,08.
    efd2: Exciter voltage at which exciter saturation is defined (EFD2) (> 0).  Typical value = 2,33.
    seefd2: Exciter saturation function value at the corresponding exciter voltage, EFD2 (SE[EFD2]) (>= 0).  Typical
      value = 0,27.
    vemin: Minimum exciter voltage output (VEMIN) (<= 0).  Typical value = 0.
    oelin: OEL input (OELin). true = LV gate false = subtract from error signal. Typical value = true.
    uelin: UEL input (UELin). true = HV gate false = add to error signal. Typical value = true.
    """

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

    kp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ki: float = Field(
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

    td: int = Field(
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

    ke: float = Field(
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

    tf: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efd1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    seefd1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efd2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    seefd2: float = Field(
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

    oelin: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    uelin: bool = Field(
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
