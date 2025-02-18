"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
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
    PositionPoints: Sequence of position points describing this location, expressed in coordinate system
      `Location.CoordinateSystem`.
    PowerSystemResources: All power system resources at this location.
    mainAddress: Main address of the location.
    """

    CoordinateSystem: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    PositionPoints: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    PowerSystemResources: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    mainAddress: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.GL,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
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
            Profile.GL,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.GL
