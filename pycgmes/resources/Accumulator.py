"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .Measurement import Measurement


@dataclass(config=DataclassConfig)
class Accumulator(Measurement, ModuleType):
    """
    Accumulator represents an accumulated (counted) Measurement, e.g. an energy value.

    AccumulatorValues: The values connected to this measurement.
    LimitSets: A measurement may have zero or more limit ranges defined for it.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return Accumulator(*args, **kwargs)

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # AccumulatorValues : list = Field(default_factory=list, in_profiles = [Profile.OP, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # LimitSets : list = Field(default_factory=list, in_profiles = [Profile.OP, ])

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
# "import Accumulator"
# work as well as
# "from Accumulator import Accumulator".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = Accumulator
