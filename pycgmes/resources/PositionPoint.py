"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Base import Base


@dataclass
class PositionPoint(Base):
    """
    Set of spatial coordinates that determine a point, defined in the coordinate system specified in
      'Location.CoordinateSystem'. Use a single position point instance to describe a point-oriented location. Use a
      sequence of position points to describe a line-oriented object (physical location of non-point oriented
      objects like cables or lines), or area of an object (like a substation or a geographical zone - in this case,
      have first and last position point with the same values).

    Location: Location described by this position point.
    sequenceNumber: Zero-relative sequence number of this point within a series of points.
    xPosition: X axis position.
    yPosition: Y axis position.
    zPosition: (if applicable) Z axis position.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    Location: Optional[str] = None  # Type M:1 in CIM
    sequenceNumber: int = 0  # Type #Integer in CIM
    xPosition: str = ""  # Type #String in CIM
    yPosition: str = ""  # Type #String in CIM
    zPosition: str = ""  # Type #String in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PositionPoint\n"
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
            "Location": [
                self.profiles.GL.value,
            ],
            "sequenceNumber": [
                self.profiles.GL.value,
            ],
            "xPosition": [
                self.profiles.GL.value,
            ],
            "yPosition": [
                self.profiles.GL.value,
            ],
            "zPosition": [
                self.profiles.GL.value,
            ],
        }
