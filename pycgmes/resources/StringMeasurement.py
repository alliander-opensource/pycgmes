"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Measurement import Measurement


@dataclass(config=DataclassConfig)
class StringMeasurement(Measurement):
    """
    StringMeasurement represents a measurement with values of type string.

    StringMeasurementValues: The values connected to this measurement.
    """

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # StringMeasurementValues : list = Field(default_factory=list, in_profiles = [Profile.OP, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }
