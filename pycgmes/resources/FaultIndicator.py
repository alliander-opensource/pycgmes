"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .AuxiliaryEquipment import AuxiliaryEquipment


@dataclass(config=DataclassConfig)
class FaultIndicator(AuxiliaryEquipment, ModuleType):
    """
    A FaultIndicator is typically only an indicator (which may or may not be remotely monitored), and not a piece of
      equipment that actually initiates a protection event. It is used for FLISR (Fault Location, Isolation and
      Restoration) purposes, assisting with the dispatch of crews to "most likely" part of the network (i.e. assists
      with determining circuit section where the fault most likely happened).

    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return FaultIndicator(*args, **kwargs)

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
# "import FaultIndicator"
# work as well as
# "from FaultIndicator import FaultIndicator".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = FaultIndicator
