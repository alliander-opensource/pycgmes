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
class Diagram(IdentifiedObject):
    """
    The diagram being exchanged. The coordinate system is a standard Cartesian coordinate system and the orientation
      attribute defines the orientation. The initial view related attributes can be used to specify an initial view
      with the x,y coordinates of the diagonal points.

    DiagramElements: A diagram is made up of multiple diagram objects.
    DiagramStyle: A Diagram may have a DiagramStyle.
    orientation: Coordinate system orientation of the diagram. A positive orientation gives standard `right-hand`
      orientation, with negative orientation indicating a `left-hand` orientation. For 2D diagrams, a
      positive orientation will result in X values increasing from left to right and Y values
      increasing from bottom to top. A negative orientation gives the `left-hand` orientation (favoured
      by computer graphics displays) with X values increasing from left to right and Y values
      increasing from top to bottom.
    x1InitialView: X coordinate of the first corner of the initial view.
    x2InitialView: X coordinate of the second corner of the initial view.
    y1InitialView: Y coordinate of the first corner of the initial view.
    y2InitialView: Y coordinate of the second corner of the initial view.
    """

    DiagramElements: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.DL,
            ],
            "is_used": False,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    DiagramStyle: Optional[str] = Field(
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

    orientation: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.DL,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": True,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    x1InitialView: float = Field(
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

    x2InitialView: float = Field(
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

    y1InitialView: float = Field(
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

    y2InitialView: float = Field(
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
