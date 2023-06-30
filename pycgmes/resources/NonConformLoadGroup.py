"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .LoadGroup import LoadGroup


@dataclass(config=DataclassConfig)
class NonConformLoadGroup(LoadGroup):
    """
    Loads that do not follow a daily and seasonal load variation pattern.

    EnergyConsumers: Conform loads assigned to this ConformLoadGroup.
    NonConformLoadSchedules: The NonConformLoadSchedules in the NonConformLoadGroup.
    """

    # *Association not used*
    # Type M:1..n in CIM  # pylint: disable-next=line-too-long
    # EnergyConsumers : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # NonConformLoadSchedules : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
