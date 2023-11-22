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
class ExcDC1A(ExcitationSystemDynamics):
    """
    Modified IEEE DC1A direct current commutator exciter with speed input and without underexcitation limiters (UEL)
      inputs.

    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 46.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical value = 0.
    ta: Voltage regulator time constant (Ta) (> 0).  Typical value = 0,06.
    tb: Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.
    tc: Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.
    vrmax: Maximum voltage regulator output (Vrmax) (> ExcDC1A.vrmin).  Typical value = 1.
    vrmin: Minimum voltage regulator output (Vrmin) (< 0 and < ExcDC1A.vrmax).  Typical value = -0,9.
    ke: Exciter constant related to self-excited field (Ke).  Typical value = 0.
    te: Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 0,46.
    kf: Excitation control system stabilizer gain (Kf) (>= 0).  Typical value = 0,1.
    tf: Excitation control system stabilizer time constant (Tf) (> 0).  Typical value = 1.
    efd1: Exciter voltage at which exciter saturation is defined (Efd1) (> 0).  Typical value = 3,1.
    seefd1: Exciter saturation function value at the corresponding exciter voltage, Efd1 (Se[Eefd1]) (>= 0).  Typical
      value = 0,33.
    efd2: Exciter voltage at which exciter saturation is defined (Efd2) (> 0).  Typical value = 2,3.
    seefd2: Exciter saturation function value at the corresponding exciter voltage, Efd2 (Se[Eefd2]) (>= 0).  Typical
      value = 0,1.
    exclim: (exclim).  IEEE standard is ambiguous about lower limit on exciter output.  true = a lower limit of zero is
      applied to integrator output false = a lower limit of zero is not applied to integrator output.
      Typical value = true.
    efdmin: Minimum voltage exciter output limiter (Efdmin) (< ExcDC1A.edfmax).  Typical value = -99.
    efdmax: Maximum voltage exciter output limiter (Efdmax) (> ExcDC1A.efdmin).  Typical value = 99.
    """

    ka: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    ks: float = Field(
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

    ke: float = Field(
        default=0.0,
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

    kf: float = Field(
        default=0.0,
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

    efd1: float = Field(
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

    efd2: float = Field(
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

    exclim: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    efdmin: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    efdmax: float = Field(
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
