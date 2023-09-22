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
class NonlinearShuntCompensatorPoint(Base, ModuleType):
    """
    A non linear shunt compensator bank or section admittance value. The number of NonlinearShuntCompenstorPoint
      instances associated with a NonlinearShuntCompensator shall be equal to ShuntCompensator.maximumSections.
      ShuntCompensator.sections shall only be set to one of the NonlinearShuntCompenstorPoint.sectionNumber. There
      is no interpolation between NonlinearShuntCompenstorPoint-s.

    NonlinearShuntCompensator: Non-linear shunt compensator owning this point.
    b: Positive sequence shunt (charging) susceptance per section.
    g: Positive sequence shunt (charging) conductance per section.
    sectionNumber: The number of the section.
    b0: Zero sequence shunt (charging) susceptance per section.
    g0: Zero sequence shunt (charging) conductance per section.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return NonlinearShuntCompensatorPoint(*args, **kwargs)

    NonlinearShuntCompensator: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    b: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    g: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    sectionNumber: int = Field(
        default=0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    b0: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    g0: float = Field(
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
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import NonlinearShuntCompensatorPoint"
# work as well as
# "from NonlinearShuntCompensatorPoint import NonlinearShuntCompensatorPoint".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = NonlinearShuntCompensatorPoint
