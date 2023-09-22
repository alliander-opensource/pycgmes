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

from .AnalogControl import AnalogControl


@dataclass(config=DataclassConfig)
class SetPoint(AnalogControl, ModuleType):
    """
    An analog control that issues a set point value.

    normalValue: Normal value for Control.value e.g. used for percentage scaling.
    value: The value representing the actuator output.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return SetPoint(*args, **kwargs)

    normalValue: float = Field(
        default=0.0,
        in_profiles=[
            Profile.OP,
        ],
    )

    value: float = Field(
        default=0.0,
        in_profiles=[
            Profile.OP,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import SetPoint"
# work as well as
# "from SetPoint import SetPoint".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = SetPoint
