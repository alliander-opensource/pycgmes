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
class StringMeasurement(Measurement, ModuleType):
    """
    StringMeasurement represents a measurement with values of type string.

    StringMeasurementValues: The values connected to this measurement.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return StringMeasurement(*args, **kwargs)

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # StringMeasurementValues : list = Field(default_factory=list, in_profiles = [Profile.OP, ])

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
# "import StringMeasurement"
# work as well as
# "from StringMeasurement import StringMeasurement".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = StringMeasurement
