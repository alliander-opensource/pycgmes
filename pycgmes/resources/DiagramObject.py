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

    Diagram: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DL,
        ],
    )

    drawingOrder: int = Field(
        default=0,
        in_profiles=[
            Profile.DL,
        ],
    )

    isPolygon: bool = Field(
        default=False,
        in_profiles=[
            Profile.DL,
        ],
    )

    offsetX: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DL,
        ],
    )

    offsetY: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DL,
        ],
    )

    rotation: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DL,
        ],
    )

    IdentifiedObject: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DL,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # DiagramObjectPoints : list = Field(default_factory=list, in_profiles = [Profile.DL, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # VisibilityLayers : list = Field(default_factory=list, in_profiles = [Profile.DL, ])

    DiagramObjectStyle: Optional[str] = Field(
        default=None,
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
