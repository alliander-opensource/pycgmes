"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

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
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # StyledObjects : list = Field(default_factory=list, in_profiles = [Profile.DL, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DL,
        }
