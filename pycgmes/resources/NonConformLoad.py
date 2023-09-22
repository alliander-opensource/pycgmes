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
class NonConformLoad(EnergyConsumer, ModuleType):
    """
    NonConformLoad represents loads that do not follow a daily load change pattern and whose changes are not correlated
      with the daily load change pattern.

    LoadGroup: Group of this ConformLoad.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return NonConformLoad(*args, **kwargs)

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
# "import NonConformLoad"
# work as well as
# "from NonConformLoad import NonConformLoad".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = NonConformLoad
