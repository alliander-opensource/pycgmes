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
from .AnalogControl import AnalogControl


@dataclass(config=DataclassConfig)
class SetPoint(AnalogControl):
    """
    An analog control that issues a set point value.

    normalValue: Normal value for Control.value e.g. used for percentage scaling.
    value: The value representing the actuator output.
    """

    normalValue: float = Field(
        default=0.0,
        in_profiles=[
            Profile.OP,
        ],
    )

    value: float = Field(
        default=0.0,
        in_profiles=[
            Profile.OP,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }
