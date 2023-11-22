# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcIEEEDC2A(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type DC2A model. This model represents field-controlled DC commutator exciters with continuously
      acting voltage regulators having supplies obtained from the generator or auxiliary bus.  It differs from the
      type DC1A model only in the voltage regulator output limits, which are now proportional to terminal voltage
      VT. It is representative of solid-state replacements for various forms of older mechanical and rotating
      amplifier regulating equipment connected to DC commutator exciters. Reference: IEEE 421.5-2005, 5.2.

    efd1: Exciter voltage at which exciter saturation is defined (EFD1) (> 0).  Typical value = 3,05.
    efd2: Exciter voltage at which exciter saturation is defined (EFD2) (> 0).  Typical value = 2,29.
    exclim: (exclim).  IEEE standard is ambiguous about lower limit on exciter output. Typical value = - 999  which
      means that there is no limit applied.
    ka: Voltage regulator gain (KA) (> 0).  Typical value = 300.
    ke: Exciter constant related to self-excited field (KE).  Typical value = 1.
    kf: Excitation control system stabilizer gain (KF) (>= 0).  Typical value = 0,1.
    seefd1: Exciter saturation function value at the corresponding exciter voltage, EFD1 (SE[EFD1]) (>= 0).  Typical
      value = 0,279.
    seefd2: Exciter saturation function value at the corresponding exciter voltage, EFD2 (SE[EFD2]) (>= 0).  Typical
      value = 0,117.
    ta: Voltage regulator time constant (TA) (> 0).  Typical value = 0,01.
    tb: Voltage regulator time constant (TB) (>= 0).  Typical value = 0.
    tc: Voltage regulator time constant (TC) (>= 0).  Typical value = 0.
    te: Exciter time constant, integration rate associated with exciter control (TE) (> 0).  Typical value = 1,33.
    tf: Excitation control system stabilizer time constant (TF) (> 0).  Typical value = 0,675.
    uelin: UEL input (uelin). true = input is connected to the HV gate false = input connects to the error signal.
      Typical value = true.
    vrmax: Maximum voltage regulator output (VRMAX)(> ExcIEEEDC2A.vrmin).  Typical value = 4,95.
    vrmin: Minimum voltage regulator output (VRMIN) (< 0 and < ExcIEEEDC2A.vrmax).  Typical value = -4,9.
    """

    efd1: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    efd2: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    exclim: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    ka: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    ke: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    kf: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    seefd1: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    seefd2: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    ta: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tb: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tc: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    te: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tf: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    uelin: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    vrmax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    vrmin: float = Field(
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
