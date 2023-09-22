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
class Fuse(Switch, ModuleType):
    """
    An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of
      overcurrent through it. A fuse is considered a switching device because it breaks current.

    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return Fuse(*args, **kwargs)

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
# "import Fuse"
# work as well as
# "from Fuse import Fuse".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = Fuse
