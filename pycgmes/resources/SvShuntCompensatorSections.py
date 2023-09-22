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
class SvShuntCompensatorSections(Base, ModuleType):
    """
    State variable for the number of sections in service for a shunt compensator.

    ShuntCompensator: The shunt compensator for which the state applies.
    sections: The number of sections in service as a continuous variable. The attribute shall be a positive value or
      zero. To get integer value scale with ShuntCompensator.bPerSection.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return SvShuntCompensatorSections(*args, **kwargs)

    ShuntCompensator: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.SV,
        ],
    )

    sections: float = Field(
        default=0.0,
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
# "import SvShuntCompensatorSections"
# work as well as
# "from SvShuntCompensatorSections import SvShuntCompensatorSections".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = SvShuntCompensatorSections
