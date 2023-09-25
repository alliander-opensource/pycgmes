"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class Diagram(IdentifiedObject):
    """
    The diagram being exchanged. The coordinate system is a standard Cartesian coordinate system and the orientation
      attribute defines the orientation. The initial view related attributes can be used to specify an initial view
      with the x,y coordinates of the diagonal points.

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
    DiagramElements: A diagram is made up of multiple diagram objects.
    DiagramStyle: A Diagram may have a DiagramStyle.
    """

    orientation: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DL,
        ],
    )

    x1InitialView: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DL,
        ],
    )

    x2InitialView: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DL,
        ],
    )

    y1InitialView: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DL,
        ],
    )

    y2InitialView: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DL,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # DiagramElements : list = Field(default_factory=list, in_profiles = [Profile.DL, ])

    DiagramStyle: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DL,
        ],
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
