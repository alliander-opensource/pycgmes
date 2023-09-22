"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class DynamicsFunctionBlock(IdentifiedObject, ModuleType):
    """
    Abstract parent class for all Dynamics function blocks.

    enabled: Function block used indicator. true = use of function block is enabled false = use of function block is
      disabled.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return DynamicsFunctionBlock(*args, **kwargs)

    enabled: bool = Field(
        default=False,
        in_profiles=[
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
            Profile.DY,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import DynamicsFunctionBlock"
# work as well as
# "from DynamicsFunctionBlock import DynamicsFunctionBlock".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = DynamicsFunctionBlock
