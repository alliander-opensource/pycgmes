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
        json_schema_extra={
            "in_profiles": [
                Profile.DL,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": True,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    DiagramObjectGluePoint: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DL,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": True,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    sequenceNumber: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DL,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "Integer",
        },
    )

    xPosition: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DL,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "Float",
        },
    )

    yPosition: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DL,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "Float",
        },
    )

    zPosition: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DL,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "Float",
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
