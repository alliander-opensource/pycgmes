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

from .EarthFaultCompensator import EarthFaultCompensator


@dataclass(config=DataclassConfig)
class GroundingImpedance(EarthFaultCompensator, ModuleType):
    """
    A fixed impedance device used for grounding.

    x: Reactance of device.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return GroundingImpedance(*args, **kwargs)

    x: float = Field(
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
# "import GroundingImpedance"
# work as well as
# "from GroundingImpedance import GroundingImpedance".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = GroundingImpedance
