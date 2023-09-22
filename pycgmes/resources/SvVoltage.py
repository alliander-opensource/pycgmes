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
class SvVoltage(Base, ModuleType):
    """
    State variable for voltage.

    angle: The voltage angle of the topological node complex voltage with respect to system reference.
    v: The voltage magnitude at the topological node. The attribute shall be a positive value.
    TopologicalNode: The topological node associated with the voltage state.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return SvVoltage(*args, **kwargs)

    angle: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SV,
        ],
    )

    v: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SV,
        ],
    )

    TopologicalNode: Optional[str] = Field(
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
# "import SvVoltage"
# work as well as
# "from SvVoltage import SvVoltage".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = SvVoltage
