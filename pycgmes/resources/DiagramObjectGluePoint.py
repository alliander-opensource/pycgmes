# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic.dataclasses import dataclass

from ..utils.base import Base
from ..utils.profile import BaseProfile, Profile


@dataclass
class DiagramObjectGluePoint(Base):
    """
    This is used for grouping diagram object points from different diagram objects that are considered to be glued
      together in a diagram even if they are not at the exact same coordinates.

    DiagramObjectPoints: A diagram object glue point is associated with 2 or more object points that are considered to
      be `glued` together.
    """

    # *Association not used*
    # Type M:2..n in CIM
    # DiagramObjectPoints : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DL, ]}) # noqa: E501

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DL,
        }
