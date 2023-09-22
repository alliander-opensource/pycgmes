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

from .Limit import Limit


@dataclass(config=DataclassConfig)
class AccumulatorLimit(Limit, ModuleType):
    """
    Limit values for Accumulator measurements.

    value: The value to supervise against. The value is positive.
    LimitSet: The set of limits.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return AccumulatorLimit(*args, **kwargs)

    value: int = Field(
        default=0,
        in_profiles=[
            Profile.OP,
        ],
    )

    LimitSet: Optional[str] = Field(
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
# "import AccumulatorLimit"
# work as well as
# "from AccumulatorLimit import AccumulatorLimit".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = AccumulatorLimit
