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
from .LoadDynamics import LoadDynamics


@dataclass
class LoadGenericNonLinear(LoadDynamics):
    """
    Generic non-linear dynamic (GNLD) load. This model can be used in mid-term and long-term voltage stability
      simulations (i.e., to study voltage collapse), as it can replace a more detailed representation of aggregate
      load, including induction motors, thermostatically controlled and static loads.

    genericNonLinearLoadModelType: Type of generic non-linear load model.
    tp: Time constant of lag function of active power (TP) (> 0).
    tq: Time constant of lag function of reactive power (TQ) (> 0).
    ls: Steady state voltage index for active power (LS).
    lt: Transient voltage index for active power (LT).
    bs: Steady state voltage index for reactive power (BS).
    bt: Transient voltage index for reactive power (BT).
    """

    genericNonLinearLoadModelType: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tp: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tq: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    ls: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    lt: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    bs: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    bt: float = Field(
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
