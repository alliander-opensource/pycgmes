"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .EnergyArea import EnergyArea


@dataclass(config=DataclassConfig)
class LoadArea(EnergyArea, ModuleType):
    """
    The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow
      load scaling.

    SubLoadAreas: The SubLoadAreas in the LoadArea.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return LoadArea(*args, **kwargs)

    # *Association not used*
    # Type M:1..n in CIM  # pylint: disable-next=line-too-long
    # SubLoadAreas : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import LoadArea"
# work as well as
# "from LoadArea import LoadArea".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = LoadArea
