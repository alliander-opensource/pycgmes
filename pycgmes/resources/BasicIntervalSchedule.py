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

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class BasicIntervalSchedule(IdentifiedObject, ModuleType):
    """
    Schedule of values at points in time.

    startTime: The time for the first time point.  The value can be a time of day, not a specific date.
    value1Unit: Value1 units of measure.
    value2Unit: Value2 units of measure.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return BasicIntervalSchedule(*args, **kwargs)

    startTime: str = Field(
        default="",
        in_profiles=[
            Profile.EQ,
        ],
    )

    value1Unit: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    value2Unit: Optional[str] = Field(
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
# "import BasicIntervalSchedule"
# work as well as
# "from BasicIntervalSchedule import BasicIntervalSchedule".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = BasicIntervalSchedule
