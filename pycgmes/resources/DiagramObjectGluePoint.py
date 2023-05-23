"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .Base import Base


@dataclass
class DiagramObjectGluePoint(Base):
    """
    This is used for grouping diagram object points from different diagram objects that are considered to be glued
      together in a diagram even if they are not at the exact same coordinates.

    DiagramObjectPoints: A diagram object glue point is associated with 2 or more object points that are considered to
      be `glued` together.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # DiagramObjectPoints : list = field(default_factory=list)  # Type M:2..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=DiagramObjectGluePoint\n"
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
            "DiagramObjectPoints": [
                self.profiles.DL.value,
            ],
        }
