"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .EnergyConsumer import EnergyConsumer


@dataclass(config=DataclassConfig)
class ConformLoad(EnergyConsumer, ModuleType):
    """
    ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load
      with a system load.

    LoadGroup: Group of this ConformLoad.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return ConformLoad(*args, **kwargs)

    LoadGroup: Optional[str] = Field(
        default=None,
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
            Profile.SSH,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import ConformLoad"
# work as well as
# "from ConformLoad import ConformLoad".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = ConformLoad
