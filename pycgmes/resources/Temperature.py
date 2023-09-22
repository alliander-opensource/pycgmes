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
class Temperature(Base, ModuleType):
    """
    Value of temperature in degrees Celsius.

    multiplier:
    unit:
    value:
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return Temperature(*args, **kwargs)

    multiplier: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.SC,
            Profile.DY,
        ],
    )

    unit: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.SC,
            Profile.DY,
        ],
    )

    value: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.SC,
            Profile.DY,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import Temperature"
# work as well as
# "from Temperature import Temperature".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = Temperature
