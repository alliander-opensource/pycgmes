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
class Command(Control, ModuleType):
    """
    A Command is a discrete control used for supervisory control.

    normalValue: Normal value for Control.value e.g. used for percentage scaling.
    value: The value representing the actuator output.
    ValueAliasSet: The ValueAliasSet used for translation of a Control value to a name.
    DiscreteValue: The MeasurementValue that is controlled.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return Command(*args, **kwargs)

    normalValue: int = Field(
        default=0,
        in_profiles=[
            Profile.OP,
        ],
    )

    value: int = Field(
        default=0,
        in_profiles=[
            Profile.OP,
        ],
    )

    ValueAliasSet: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.OP,
        ],
    )

    DiscreteValue: Optional[str] = Field(
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
# "import Command"
# work as well as
# "from Command import Command".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = Command
