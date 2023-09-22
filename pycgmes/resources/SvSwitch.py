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
class SvSwitch(Base, ModuleType):
    """
    State variable for switch.

    open: The attribute tells if the computed state of the switch is considered open.
    Switch: The switch associated with the switch state.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return SvSwitch(*args, **kwargs)

    open: bool = Field(
        default=False,
        in_profiles=[
            Profile.SV,
        ],
    )

    Switch: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.SV,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.SV,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import SvSwitch"
# work as well as
# "from SvSwitch import SvSwitch".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = SvSwitch
