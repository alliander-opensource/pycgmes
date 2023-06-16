"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class DiagramObject(IdentifiedObject):
    """
    An object that defines one or more points in a given space. This object can be associated with anything that
      specializes IdentifiedObject. For single line diagrams such objects typically include such items as analog
      values, breakers, disconnectors, power transformers, and transmission lines.

    Diagram: A diagram object is part of a diagram.
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
    IdentifiedObject: The domain object to which this diagram object is associated.
    DiagramObjectPoints: A diagram object can have 0 or more points to reflect its layout position, routing (for
      polylines) or boundary (for polygons).
    VisibilityLayers: A diagram object can be part of multiple visibility layers.
    DiagramObjectStyle: A diagram object has a style associated that provides a reference for the style used in the
      originating system.
    """

    Diagram: Optional[str] = None  # Type M:1 in CIM
    drawingOrder: int = 0  # Type #Integer in CIM
    isPolygon: bool = False  # Type #Boolean in CIM
    offsetX: float = 0.0  # Type #Float in CIM
    offsetY: float = 0.0  # Type #Float in CIM
    rotation: float = 0.0  # Type #AngleDegrees in CIM
    IdentifiedObject: Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # DiagramObjectPoints : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # VisibilityLayers : list = field(default_factory=list)  # Type M:0..n in CIM
    DiagramObjectStyle: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=DiagramObject"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
        )

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                Profile.DL.value,
            ],
            # Attributes
            "Diagram": [
                Profile.DL.value,
            ],
            "drawingOrder": [
                Profile.DL.value,
            ],
            "isPolygon": [
                Profile.DL.value,
            ],
            "offsetX": [
                Profile.DL.value,
            ],
            "offsetY": [
                Profile.DL.value,
            ],
            "rotation": [
                Profile.DL.value,
            ],
            "IdentifiedObject": [
                Profile.DL.value,
            ],
            "DiagramObjectPoints": [
                Profile.DL.value,
            ],
            "VisibilityLayers": [
                Profile.DL.value,
            ],
            "DiagramObjectStyle": [
                Profile.DL.value,
            ],
        }
