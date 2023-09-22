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

from .MechanicalLoadDynamics import MechanicalLoadDynamics


@dataclass(config=DataclassConfig)
class MechLoad1(MechanicalLoadDynamics, ModuleType):
    """
    Mechanical load model type 1.

    a: Speed squared coefficient (a).
    b: Speed coefficient (b).
    d: Speed to the exponent coefficient (d).
    e: Exponent (e).
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return MechLoad1(*args, **kwargs)

    a: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    b: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    d: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    e: float = Field(
        default=0.0,
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
# "import MechLoad1"
# work as well as
# "from MechLoad1 import MechLoad1".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = MechLoad1
