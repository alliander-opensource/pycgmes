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

from .LimitSet import LimitSet


@dataclass(config=DataclassConfig)
class AnalogLimitSet(LimitSet, ModuleType):
    """
    An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement.

    Measurements: The Measurements using the LimitSet.
    Limits: The limit values used for supervision of Measurements.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return AnalogLimitSet(*args, **kwargs)

    Measurements: list = Field(
        default_factory=list,
        in_profiles=[
            Profile.OP,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # Limits : list = Field(default_factory=list, in_profiles = [Profile.OP, ])

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
# "import AnalogLimitSet"
# work as well as
# "from AnalogLimitSet import AnalogLimitSet".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = AnalogLimitSet
