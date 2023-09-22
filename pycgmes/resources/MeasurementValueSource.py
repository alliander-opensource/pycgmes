"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class MeasurementValueSource(IdentifiedObject, ModuleType):
    """
    MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to
      use the MeasurementValueSource attributes are defined in IEC 61970-301.

    MeasurementValues: The MeasurementValues updated by the source.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return MeasurementValueSource(*args, **kwargs)

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # MeasurementValues : list = Field(default_factory=list, in_profiles = [Profile.OP, ])

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
# "import MeasurementValueSource"
# work as well as
# "from MeasurementValueSource import MeasurementValueSource".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = MeasurementValueSource
