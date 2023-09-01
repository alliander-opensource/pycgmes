"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PowerSystemResource import PowerSystemResource


@dataclass(config=DataclassConfig)
class SolarPowerPlant(PowerSystemResource):
    """
    Solar power plant.

    SolarGeneratingUnits: A solar generating unit or units may be a member of a solar power plant.
    """

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # SolarGeneratingUnits : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
