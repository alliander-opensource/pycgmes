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
class DiagramObjectStyle(IdentifiedObject, ModuleType):
    """
    A reference to a style used by the originating system for a diagram object.  A diagram object style describes
      information such as line thickness, shape such as circle or rectangle etc, and colour.

    StyledObjects: A style can be assigned to multiple diagram objects.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return DiagramObjectStyle(*args, **kwargs)

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # StyledObjects : list = Field(default_factory=list, in_profiles = [Profile.DL, ])

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
# "import DiagramObjectStyle"
# work as well as
# "from DiagramObjectStyle import DiagramObjectStyle".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = DiagramObjectStyle
