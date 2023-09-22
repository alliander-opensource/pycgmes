"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class DiagramStyle(IdentifiedObject, ModuleType):
    """
    The diagram style refers to a style used by the originating system for a diagram.  A diagram style describes
      information such as schematic, geographic, etc.

    Diagram: A DiagramStyle can be used by many Diagrams.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return DiagramStyle(*args, **kwargs)

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # Diagram : list = Field(default_factory=list, in_profiles = [Profile.DL, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DL,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import DiagramStyle"
# work as well as
# "from DiagramStyle import DiagramStyle".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = DiagramStyle
