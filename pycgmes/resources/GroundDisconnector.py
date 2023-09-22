"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .Switch import Switch


@dataclass(config=DataclassConfig)
class GroundDisconnector(Switch, ModuleType):
    """
    A manually operated or motor operated mechanical switching device used for isolating a circuit or equipment from
      ground.

    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return GroundDisconnector(*args, **kwargs)

    # No attributes defined for this class.

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SSH,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import GroundDisconnector"
# work as well as
# "from GroundDisconnector import GroundDisconnector".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = GroundDisconnector
