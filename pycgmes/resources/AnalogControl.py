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

from .Control import Control


@dataclass(config=DataclassConfig)
class AnalogControl(Control, ModuleType):
    """
    An analog control used for supervisory control.

    maxValue: Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs.
    minValue: Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs.
    AnalogValue: The MeasurementValue that is controlled.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return AnalogControl(*args, **kwargs)

    maxValue: float = Field(
        default=0.0,
        in_profiles=[
            Profile.OP,
        ],
    )

    minValue: float = Field(
        default=0.0,
        in_profiles=[
            Profile.OP,
        ],
    )

    AnalogValue: Optional[str] = Field(
        default=None,
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
# "import AnalogControl"
# work as well as
# "from AnalogControl import AnalogControl".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = AnalogControl
