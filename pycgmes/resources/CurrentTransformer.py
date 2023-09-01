"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Sensor import Sensor


@dataclass(config=DataclassConfig)
class CurrentTransformer(Sensor):
    """
    Instrument transformer used to measure electrical qualities of the circuit that is being protected and/or monitored.
      Typically used as current transducer for the purpose of metering or protection. A typical secondary current
      rating would be 5A.

    """

    # No attributes defined for this class.

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
