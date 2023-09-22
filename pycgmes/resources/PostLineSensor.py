"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .Sensor import Sensor


@dataclass(config=DataclassConfig)
class PostLineSensor(Sensor, ModuleType):
    """
    A sensor used mainly in overhead distribution networks as the source of both current and voltage measurements.

    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return PostLineSensor(*args, **kwargs)

    # No attributes defined for this class.

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
# "import PostLineSensor"
# work as well as
# "from PostLineSensor import PostLineSensor".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = PostLineSensor
