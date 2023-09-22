"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from ..utils.base import Base


@dataclass(config=DataclassConfig)
class DiagramObjectGluePoint(Base, ModuleType):
    """
    This is used for grouping diagram object points from different diagram objects that are considered to be glued
      together in a diagram even if they are not at the exact same coordinates.

    DiagramObjectPoints: A diagram object glue point is associated with 2 or more object points that are considered to
      be `glued` together.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return DiagramObjectGluePoint(*args, **kwargs)

    # *Association not used*
    # Type M:2..n in CIM  # pylint: disable-next=line-too-long
    # DiagramObjectPoints : list = Field(default_factory=list, in_profiles = [Profile.DL, ])

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
# "import DiagramObjectGluePoint"
# work as well as
# "from DiagramObjectGluePoint import DiagramObjectGluePoint".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = DiagramObjectGluePoint
