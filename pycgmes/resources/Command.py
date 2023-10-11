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
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .Control import Control


@dataclass(config=DataclassConfig)
class Command(Control):
    """
    A Command is a discrete control used for supervisory control.

    normalValue: Normal value for Control.value e.g. used for percentage scaling.
    value: The value representing the actuator output.
    ValueAliasSet: The ValueAliasSet used for translation of a Control value to a name.
    DiscreteValue: The MeasurementValue that is controlled.
    """

    normalValue: int = Field(
        default=0,
        in_profiles=[
            Profile.OP,
        ],
    )

    value: int = Field(
        default=0,
        in_profiles=[
            Profile.OP,
        ],
    )

    ValueAliasSet: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.OP,
        ],
    )

    DiscreteValue: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.OP,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }
