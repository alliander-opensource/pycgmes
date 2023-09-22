"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .ConductingEquipment import ConductingEquipment


@dataclass(config=DataclassConfig)
class Conductor(ConductingEquipment, ModuleType):
    """
    Combination of conducting material with consistent electrical characteristics, building a single electrical system,
      used to carry current between points in the power system.

    length: Segment length for calculating line section capabilities.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return Conductor(*args, **kwargs)

    length: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SC,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import Conductor"
# work as well as
# "from Conductor import Conductor".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = Conductor
