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
from .PFVArControllerType2Dynamics import PFVArControllerType2Dynamics


@dataclass
class PFVArType2IEEEVArController(PFVArControllerType2Dynamics):
    """
    IEEE VAR controller type 2 which is a summing point type controller. It makes up the outside loop of a two-loop
      system. This controller is implemented as a slow PI type controller, and the voltage regulator forms the inner
      loop and is implemented as a fast controller. Reference: IEEE 421.5-2005, 11.5.

    qref: Reactive power reference (QREF).
    vref: Voltage regulator reference (VREF).
    vclmt: Maximum output of the pf controller (VCLMT).
    kp: Proportional gain of the pf controller (KP).
    ki: Integral gain of the pf controller (KI).
    vs: Generator sensing voltage (VS).
    exlon: Overexcitation or under excitation flag (EXLON) true = 1 (not in the overexcitation or underexcitation state,
      integral action is active) false = 0 (in the overexcitation or underexcitation state, so integral
      action is disabled to allow the limiter to play its role).
    """

    qref: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    vref: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    vclmt: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    kp: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    ki: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    vs: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    exlon: bool = Field(
        default=False,
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
