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

from .ShuntCompensator import ShuntCompensator


@dataclass(config=DataclassConfig)
class LinearShuntCompensator(ShuntCompensator, ModuleType):
    """
    A linear shunt compensator has banks or sections with equal admittance values.

    bPerSection: Positive sequence shunt (charging) susceptance per section.
    gPerSection: Positive sequence shunt (charging) conductance per section.
    b0PerSection: Zero sequence shunt (charging) susceptance per section.
    g0PerSection: Zero sequence shunt (charging) conductance per section.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return LinearShuntCompensator(*args, **kwargs)

    bPerSection: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    gPerSection: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    b0PerSection: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    g0PerSection: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
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
# "import LinearShuntCompensator"
# work as well as
# "from LinearShuntCompensator import LinearShuntCompensator".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = LinearShuntCompensator
