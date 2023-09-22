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
class PU(Base, ModuleType):
    """
    Per Unit - a positive or negative value referred to a defined base. Values typically range from -10 to +10.

    value:
    unit:
    multiplier:
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return PU(*args, **kwargs)

    value: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
            Profile.SSH,
            Profile.DY,
        ],
    )

    unit: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.SC,
            Profile.SSH,
            Profile.DY,
        ],
    )

    multiplier: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.SC,
            Profile.SSH,
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
            Profile.SSH,
            Profile.DY,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import PU"
# work as well as
# "from PU import PU".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = PU
