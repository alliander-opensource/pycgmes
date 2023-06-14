"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class DiagramObjectGluePoint(Base):
    """
    This is used for grouping diagram object points from different diagram objects that are considered to be glued
      together in a diagram even if they are not at the exact same coordinates.

    DiagramObjectPoints: A diagram object glue point is associated with 2 or more object points that are considered to
      be `glued` together.
    """

    # *Association not used*
    # DiagramObjectPoints : list = field(default_factory=list)  # Type M:2..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=DiagramObjectGluePoint"]
            + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "DiagramObjectPoints": [
                Profile.DL.value,
            ],
        }
