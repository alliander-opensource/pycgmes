"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class DiagramObjectPoint(Base):
    """
    A point in a given space defined by 3 coordinates and associated to a diagram object.  The coordinates may be
      positive or negative as the origin does not have to be in the corner of a diagram.

    DiagramObject: The diagram object with which the points are associated.
    DiagramObjectGluePoint: The `glue` point to which this point is associated.
    sequenceNumber: The sequence position of the point, used for defining the order of points for diagram objects acting
      as a polyline or polygon with more than one point. The attribute shall be a positive value.
    xPosition: The X coordinate of this point.
    yPosition: The Y coordinate of this point.
    zPosition: The Z coordinate of this point.
    """

    DiagramObject: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DL,
        ],
    )

    DiagramObjectGluePoint: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DL,
        ],
    )

    sequenceNumber: int = Field(
        default=0,
        in_profiles=[
            Profile.DL,
        ],
    )

    xPosition: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DL,
        ],
    )

    yPosition: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DL,
        ],
    )

    zPosition: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DL,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DL,
        }
