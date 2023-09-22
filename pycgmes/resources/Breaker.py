"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .ProtectedSwitch import ProtectedSwitch


@dataclass(config=DataclassConfig)
class Breaker(ProtectedSwitch, ModuleType):
    """
    A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and
      also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions
      e.g.  those of short circuit.

    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return Breaker(*args, **kwargs)

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
# "import Breaker"
# work as well as
# "from Breaker import Breaker".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = Breaker
