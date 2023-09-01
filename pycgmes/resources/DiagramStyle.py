"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class DiagramStyle(IdentifiedObject):
    """
    The diagram style refers to a style used by the originating system for a diagram.  A diagram style describes
      information such as schematic, geographic, etc.

    Diagram: A DiagramStyle can be used by many Diagrams.
    """

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # Diagram : list = Field(default_factory=list, in_profiles = [Profile.DL, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DL,
        }
