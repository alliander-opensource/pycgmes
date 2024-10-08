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

from ..utils.base import Base
from ..utils.profile import BaseProfile, Profile


@dataclass
class AngleDegrees(Base):
    """
    Measurement of angle in degrees.

    value:
    unit:
    multiplier:
    """

    value: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DL,
                Profile.EQ,
                Profile.SC,
                Profile.SV,
                Profile.SSH,
                Profile.DY,
            ]
        },
    )

    unit: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DL,
                Profile.EQ,
                Profile.SC,
                Profile.SV,
                Profile.SSH,
                Profile.DY,
            ]
        },
    )

    multiplier: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DL,
                Profile.EQ,
                Profile.SC,
                Profile.SV,
                Profile.SSH,
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
            Profile.DL,
            Profile.EQ,
            Profile.SC,
            Profile.SV,
            Profile.SSH,
            Profile.DY,
        }
