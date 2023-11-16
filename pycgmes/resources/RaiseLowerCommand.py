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
from .AnalogControl import AnalogControl


@dataclass
class RaiseLowerCommand(AnalogControl):
    """
    An analog control that increases or decreases a set point value with pulses. Unless otherwise specified, one pulse
      moves the set point by one.

    ValueAliasSet: The ValueAliasSet used for translation of a Control value to a name.
    """

    ValueAliasSet: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
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
            Profile.OP,
        }
