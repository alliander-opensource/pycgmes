"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    orientation: Optional[str] = None  # Type M:1..1 in CIM
    x1InitialView: float = 0.0  # Type #Float in CIM
    x2InitialView: float = 0.0  # Type #Float in CIM
    y1InitialView: float = 0.0  # Type #Float in CIM
    y2InitialView: float = 0.0  # Type #Float in CIM
    # *Association not used*
    # DiagramElements : list = field(default_factory=list)  # Type M:0..n in CIM
    DiagramStyle: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=Diagram\n"
        attributes = self.__dict__
        for key, val in attributes.items():
            str_ = str_ + key + f"={val}\n"
        return str_

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                self.profiles.DL.value,
            ],
            # Attributes
            "orientation": [
                self.profiles.DL.value,
            ],
            "x1InitialView": [
                self.profiles.DL.value,
            ],
            "x2InitialView": [
                self.profiles.DL.value,
            ],
            "y1InitialView": [
                self.profiles.DL.value,
            ],
            "y2InitialView": [
                self.profiles.DL.value,
            ],
            "DiagramElements": [
                self.profiles.DL.value,
            ],
            "DiagramStyle": [
                self.profiles.DL.value,
            ],
        }
