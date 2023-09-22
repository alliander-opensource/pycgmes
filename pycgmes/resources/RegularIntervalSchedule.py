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

from .BasicIntervalSchedule import BasicIntervalSchedule


@dataclass(config=DataclassConfig)
class RegularIntervalSchedule(BasicIntervalSchedule, ModuleType):
    """
    The schedule has time points where the time between them is constant.

    TimePoints: The regular interval time point data values that define this schedule.
    timeStep: The time between each pair of subsequent regular time points in sequence order.
    endTime: The time for the last time point.  The value can be a time of day, not a specific date.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return RegularIntervalSchedule(*args, **kwargs)

    # *Association not used*
    # Type M:1..n in CIM  # pylint: disable-next=line-too-long
    # TimePoints : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    timeStep: int = Field(
        default=0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    endTime: str = Field(
        default="",
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
# "import RegularIntervalSchedule"
# work as well as
# "from RegularIntervalSchedule import RegularIntervalSchedule".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = RegularIntervalSchedule
