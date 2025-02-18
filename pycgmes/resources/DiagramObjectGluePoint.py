"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from ..utils.base import Base


@dataclass
class DiagramObjectGluePoint(Base):
    """
    This is used for grouping diagram object points from different diagram objects that are considered to be glued
      together in a diagram even if they are not at the exact same coordinates.

    DiagramObjectPoints: A diagram object glue point is associated with 2 or more object points that are considered to
      be `glued` together.
    """

    DiagramObjectPoints: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.DL,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
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
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.DL
