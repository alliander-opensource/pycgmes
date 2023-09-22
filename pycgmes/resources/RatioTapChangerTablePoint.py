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

from .TapChangerTablePoint import TapChangerTablePoint


@dataclass(config=DataclassConfig)
class RatioTapChangerTablePoint(TapChangerTablePoint, ModuleType):
    """
    Describes each tap step in the ratio tap changer tabular curve.

    RatioTapChangerTable: Table of this point.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return RatioTapChangerTablePoint(*args, **kwargs)

    RatioTapChangerTable: Optional[str] = Field(
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
# "import RatioTapChangerTablePoint"
# work as well as
# "from RatioTapChangerTablePoint import RatioTapChangerTablePoint".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = RatioTapChangerTablePoint
