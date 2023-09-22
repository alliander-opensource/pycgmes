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

from .DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics


@dataclass(config=DataclassConfig)
class DiscExcContIEEEDEC3A(DiscontinuousExcitationControlDynamics, ModuleType):
    """
    IEEE type DEC3A model. In some systems, the stabilizer output is disconnected from the regulator immediately
      following a severe fault to prevent the stabilizer from competing with action of voltage regulator during the
      first swing. Reference: IEEE 421.5-2005 12.4.

    vtmin: Terminal undervoltage comparison level (VTMIN).
    tdr: Reset time delay (TDR) (>= 0).
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return DiscExcContIEEEDEC3A(*args, **kwargs)

    vtmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tdr: int = Field(
        default=0,
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
# "import DiscExcContIEEEDEC3A"
# work as well as
# "from DiscExcContIEEEDEC3A import DiscExcContIEEEDEC3A".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = DiscExcContIEEEDEC3A
