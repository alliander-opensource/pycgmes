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
class Resistance(Base, ModuleType):
    """
    Resistance (real part of impedance).

    value:
    unit:
    multiplier:
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return Resistance(*args, **kwargs)

    value: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
            Profile.SC,
            Profile.SSH,
        ],
    )

    unit: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
            Profile.SC,
            Profile.SSH,
        ],
    )

    multiplier: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
            Profile.SC,
            Profile.SSH,
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
            Profile.SC,
            Profile.SSH,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import Resistance"
# work as well as
# "from Resistance import Resistance".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = Resistance
