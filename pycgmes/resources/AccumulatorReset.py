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
class AccumulatorReset(Control, ModuleType):
    """
    This command resets the counter value to zero.

    AccumulatorValue: The accumulator value that is reset by the command.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return AccumulatorReset(*args, **kwargs)

    AccumulatorValue: Optional[str] = Field(
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
# "import AccumulatorReset"
# work as well as
# "from AccumulatorReset import AccumulatorReset".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = AccumulatorReset
