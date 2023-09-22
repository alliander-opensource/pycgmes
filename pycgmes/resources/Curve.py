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
class Curve(IdentifiedObject, ModuleType):
    """
    A multi-purpose curve or functional relationship between an independent variable (X-axis) and dependent (Y-axis)
      variables.

    curveStyle: The style or shape of the curve.
    xUnit: The X-axis units of measure.
    y1Unit: The Y1-axis units of measure.
    y2Unit: The Y2-axis units of measure.
    CurveDatas: The point data values that define this curve.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return Curve(*args, **kwargs)

    curveStyle: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    xUnit: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    y1Unit: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    y2Unit: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:1..n in CIM  # pylint: disable-next=line-too-long
    # CurveDatas : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

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
# "import Curve"
# work as well as
# "from Curve import Curve".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = Curve
