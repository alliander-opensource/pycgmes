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

from ..utils.base import Base


@dataclass(config=DataclassConfig)
class CurveData(Base, ModuleType):
    """
    Multi-purpose data points for defining a curve.  The use of this generic class is discouraged if a more specific
      class can be used to specify the X and Y axis values along with their specific data types.

    Curve: The curve of  this curve data point.
    xvalue: The data value of the X-axis variable,  depending on the X-axis units.
    y1value: The data value of the  first Y-axis variable, depending on the Y-axis units.
    y2value: The data value of the second Y-axis variable (if present), depending on the Y-axis units.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return CurveData(*args, **kwargs)

    Curve: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    xvalue: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    y1value: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    y2value: float = Field(
        default=0.0,
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
# "import CurveData"
# work as well as
# "from CurveData import CurveData".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = CurveData
