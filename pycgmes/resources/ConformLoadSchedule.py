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
class ConformLoadSchedule(SeasonDayTypeSchedule, ModuleType):
    """
    A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for
      each unit of the period covered. This curve represents a typical pattern of load over the time period for a
      given day type and season.

    ConformLoadGroup: The ConformLoadGroup where the ConformLoadSchedule belongs.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return ConformLoadSchedule(*args, **kwargs)

    ConformLoadGroup: Optional[str] = Field(
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
# "import ConformLoadSchedule"
# work as well as
# "from ConformLoadSchedule import ConformLoadSchedule".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = ConformLoadSchedule
