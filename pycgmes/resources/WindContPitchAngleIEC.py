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
from .IdentifiedObject import IdentifiedObject


@dataclass
class WindContPitchAngleIEC(IdentifiedObject):
    """
    Pitch angle control model. Reference: IEC 61400-27-1:2015, 5.6.5.2.

    dthetamax: Maximum pitch positive ramp rate (dthetamax) (> WindContPitchAngleIEC.dthetamin). It is a type-dependent
      parameter. Unit = degrees / s.
    dthetamin: Maximum pitch negative ramp rate (dthetamin) (< WindContPitchAngleIEC.dthetamax). It is a type-dependent
      parameter. Unit = degrees / s.
    kic: Power PI controller integration gain (KIc). It is a type-dependent parameter.
    kiomega: Speed PI controller integration gain (KIomega). It is a type-dependent parameter.
    kpc: Power PI controller proportional gain (KPc). It is a type-dependent parameter.
    kpomega: Speed PI controller proportional gain (KPomega). It is a type-dependent parameter.
    kpx: Pitch cross coupling gain (KPX). It is a type-dependent parameter.
    thetamax: Maximum pitch angle (thetamax) (> WindContPitchAngleIEC.thetamin). It is a type-dependent parameter.
    thetamin: Minimum pitch angle (thetamin) (< WindContPitchAngleIEC.thetamax). It is a type-dependent parameter.
    ttheta: Pitch time constant (ttheta) (>= 0). It is a type-dependent parameter.
    WindTurbineType3IEC: Wind turbine type 3 model with which this pitch control model is associated.
    """

    dthetamax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    dthetamin: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    kic: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    kiomega: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    kpc: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    kpomega: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    kpx: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    thetamax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    thetamin: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    ttheta: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    # *Association not used*
    # Type M:1 in CIM
    # WindTurbineType3IEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
