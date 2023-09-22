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
class CurrentTransformer(Sensor, ModuleType):
    """
    Instrument transformer used to measure electrical qualities of the circuit that is being protected and/or monitored.
      Typically used as current transducer for the purpose of metering or protection. A typical secondary current
      rating would be 5A.

    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return CurrentTransformer(*args, **kwargs)

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
# "import CurrentTransformer"
# work as well as
# "from CurrentTransformer import CurrentTransformer".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = CurrentTransformer
