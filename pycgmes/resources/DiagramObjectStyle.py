"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class DiagramObjectStyle(IdentifiedObject):
    """
    A reference to a style used by the originating system for a diagram object.  A diagram object style describes
      information such as line thickness, shape such as circle or rectangle etc, and colour.

    StyledObjects: A style can be assigned to multiple diagram objects.
    """

    # *Association not used*
    # StyledObjects : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=DiagramObjectStyle"]
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
            "StyledObjects": [
                Profile.DL.value,
            ],
        }
