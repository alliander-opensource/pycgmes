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

from .SeasonDayTypeSchedule import SeasonDayTypeSchedule


@dataclass(config=DataclassConfig)
class NonConformLoadSchedule(SeasonDayTypeSchedule, ModuleType):
    """
    An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming
      loads, e.g., large industrial load or power station service (where modelled).

    NonConformLoadGroup: The NonConformLoadGroup where the NonConformLoadSchedule belongs.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return NonConformLoadSchedule(*args, **kwargs)

    NonConformLoadGroup: Optional[str] = Field(
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
# "import NonConformLoadSchedule"
# work as well as
# "from NonConformLoadSchedule import NonConformLoadSchedule".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = NonConformLoadSchedule
