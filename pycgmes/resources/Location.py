"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
class Location(IdentifiedObject):
    """
    The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in
      time. It can be defined with one or more position points (coordinates) in a given coordinate system.

    CoordinateSystem: Coordinate system used to describe position points of this location.
    mainAddress: Main address of the location.
    PowerSystemResources: All power system resources at this location.
    PositionPoints: Sequence of position points describing this location, expressed in coordinate system
      `Location.CoordinateSystem`.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    CoordinateSystem: Optional[str] = None  # Type M:1 in CIM
    mainAddress: float = 0.0  # Type #StreetAddress in CIM
    PowerSystemResources: Optional[str] = None  # Type M:1 in CIM
    # *Association not used*
    # PositionPoints : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=Location\n"
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
                self.profiles.GL.value,
            ],
            # Attributes
            "CoordinateSystem": [
                self.profiles.GL.value,
            ],
            "mainAddress": [
                self.profiles.GL.value,
            ],
            "PowerSystemResources": [
                self.profiles.GL.value,
            ],
            "PositionPoints": [
                self.profiles.GL.value,
            ],
        }
