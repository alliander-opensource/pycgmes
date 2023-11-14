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
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile


@dataclass(config=DataclassConfig)
class PositionPoint(Base):
    """
    Set of spatial coordinates that determine a point, defined in the coordinate system specified in
      'Location.CoordinateSystem'. Use a single position point instance to describe a point-oriented location. Use a
      sequence of position points to describe a line-oriented object (physical location of non-point oriented
      objects like cables or lines), or area of an object (like a substation or a geographical zone - in this case,
      have first and last position point with the same values).

    Location: Location described by this position point.
    sequenceNumber: Zero-relative sequence number of this point within a series of points.
    xPosition: X axis position.
    yPosition: Y axis position.
    zPosition: (if applicable) Z axis position.
    """

    Location: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.GL,
        ],
    )

    sequenceNumber: int = Field(
        default=0,
        in_profiles=[
            Profile.GL,
        ],
    )

    xPosition: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    yPosition: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    zPosition: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.GL,
        }
