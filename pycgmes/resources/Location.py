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
from .IdentifiedObject import IdentifiedObject


@dataclass
class Location(IdentifiedObject):
    """
    The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in
      time. It can be defined with one or more position points (coordinates) in a given coordinate system.

    CoordinateSystem: Coordinate system used to describe position points of this location.
    mainAddress: Main address of the location.
    PowerSystemResources: All power system resources at this location.
    PositionPoints: Sequence of position points describing this location, expressed in coordinate system
      `Location.CoordinateSystem`.
    """

    CoordinateSystem: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ]
        },
    )

    mainAddress: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ]
        },
    )

    PowerSystemResources: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ]
        },
    )

    # *Association not used*
    # Type M:0..n in CIM
    # PositionPoints : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.GL, ]})

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.GL,
        }
