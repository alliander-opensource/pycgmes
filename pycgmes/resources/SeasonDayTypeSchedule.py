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

from .RegularIntervalSchedule import RegularIntervalSchedule


@dataclass(config=DataclassConfig)
class SeasonDayTypeSchedule(RegularIntervalSchedule, ModuleType):
    """
    A time schedule covering a 24 hour period, with curve data for a specific type of season and day.

    DayType: DayType for the Schedule.
    Season: Season for the Schedule.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return SeasonDayTypeSchedule(*args, **kwargs)

    DayType: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    Season: Optional[str] = Field(
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
# "import SeasonDayTypeSchedule"
# work as well as
# "from SeasonDayTypeSchedule import SeasonDayTypeSchedule".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = SeasonDayTypeSchedule
