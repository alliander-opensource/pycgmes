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

from .DCEquipmentContainer import DCEquipmentContainer


@dataclass(config=DataclassConfig)
class DCLine(DCEquipmentContainer, ModuleType):
    """
    Overhead lines and/or cables connecting two or more HVDC substations.

    Region: The SubGeographicalRegion containing the DC line.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return DCLine(*args, **kwargs)

    Region: Optional[str] = Field(
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
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import DCLine"
# work as well as
# "from DCLine import DCLine".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = DCLine
