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
class DiagramObject(IdentifiedObject):
    """
    An object that defines one or more points in a given space. This object can be associated with anything that
      specializes IdentifiedObject. For single line diagrams such objects typically include such items as analog
      values, breakers, disconnectors, power transformers, and transmission lines.

    Diagram: A diagram object is part of a diagram.
    DiagramObjectPoints: A diagram object can have 0 or more points to reflect its layout position, routing (for
      polylines) or boundary (for polygons).
    DiagramObjectStyle: A diagram object has a style associated that provides a reference for the style used in the
      originating system.
    IdentifiedObject: The domain object to which this diagram object is associated.
    VisibilityLayers: A diagram object can be part of multiple visibility layers.
    drawingOrder: The drawing order of this element. The higher the number, the later the element is drawn in sequence.
      This is used to ensure that elements that overlap are rendered in the correct order.
    isPolygon: Defines whether or not the diagram objects points define the boundaries of a polygon or the routing of a
      polyline. If this value is true then a receiving application should consider the first and last
      points to be connected.
    offsetX: The offset in the X direction. This is used for defining the offset from centre for rendering an icon (the
      default is that a single point specifies the centre of the icon).  The offset is in per-unit with 0
      indicating there is no offset from the horizontal centre of the icon.  -0.5 indicates it is offset by
      50% to the left and 0.5 indicates an offset of 50% to the right.
    offsetY: The offset in the Y direction. This is used for defining the offset from centre for rendering an icon (the
      default is that a single point specifies the centre of the icon).  The offset is in per-unit with 0
      indicating there is no offset from the vertical centre of the icon.  The offset direction is
      dependent on the orientation of the diagram, with -0.5 and 0.5 indicating an offset of +/- 50% on the
      vertical axis.
    rotation: Sets the angle of rotation of the diagram object.  Zero degrees is pointing to the top of the diagram.
      Rotation is clockwise.  DiagramObject.rotation=0 has the following meaning: The connection point of
      an element which has one terminal is pointing to the top side of the diagram. The connection point
      `From side` of an element which has more than one terminal is pointing to the top side of the
      diagram. DiagramObject.rotation=90 has the following meaning: The connection point of an element
      which has one terminal is pointing to the right hand side of the diagram. The connection point `From
      side` of an element which has more than one terminal is pointing to the right hand side of the
      diagram.
    """

    Diagram: Optional[str] = Field(
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

    DiagramObjectPoints: list = Field(
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

    DiagramObjectStyle: Optional[str] = Field(
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

    IdentifiedObject: Optional[str] = Field(
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

    VisibilityLayers: list = Field(
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

    drawingOrder: int = Field(
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

    isPolygon: bool = Field(
        default=False,
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
            "attribute_class": "Boolean",
        },
    )

    offsetX: float = Field(
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

    offsetY: float = Field(
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

    rotation: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DL,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "AngleDegrees",
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
