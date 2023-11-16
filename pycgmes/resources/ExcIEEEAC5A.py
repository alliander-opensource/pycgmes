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
class ExcIEEEAC5A(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type AC5A model. The model represents a simplified model for brushless excitation systems. The
      regulator is supplied from a source, such as a permanent magnet generator, which is not affected by system
      disturbances.  Unlike other AC models, this model uses loaded rather than open circuit exciter saturation data
      in the same way as it is used for the DC models.  Because the model has been widely implemented by the
      industry, it is sometimes used to represent other types of systems when either detailed data for them are not
      available or simplified models are required. Reference: IEEE 421.5-2005, 6.5.

    ka: Voltage regulator gain (KA) (> 0).  Typical value = 400.
    ta: Voltage regulator time constant (TA) (> 0).  Typical value = 0,02.
    vrmax: Maximum voltage regulator output (VRMAX) (> 0).  Typical value = 7,3.
    vrmin: Minimum voltage regulator output (VRMIN) (< 0).  Typical value = -7,3.
    ke: Exciter constant related to self-excited field (KE).  Typical value = 1.
    te: Exciter time constant, integration rate associated with exciter control (TE) (> 0).  Typical value = 0,8.
    kf: Excitation control system stabilizer gains (KF) (>= 0).  Typical value = 0,03.
    tf1: Excitation control system stabilizer time constant (TF1) (> 0).  Typical value = 1.
    tf2: Excitation control system stabilizer time constant (TF2) (>= 0).  Typical value = 1.
    tf3: Excitation control system stabilizer time constant (TF3) (>= 0).  Typical value = 1.
    efd1: Exciter voltage at which exciter saturation is defined (EFD1) (> 0).  Typical value = 5,6.
    seefd1: Exciter saturation function value at the corresponding exciter voltage, EFD1 (SE[EFD1]) (>= 0).  Typical
      value = 0,86.
    efd2: Exciter voltage at which exciter saturation is defined (EFD2) (> 0).  Typical value = 4,2.
    seefd2: Exciter saturation function value at the corresponding exciter voltage, EFD2 (SE[EFD2]) (>= 0).  Typical
      value = 0,5.
    """

    ka: float = Field(
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

    tf1: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tf2: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tf3: int = Field(
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

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
