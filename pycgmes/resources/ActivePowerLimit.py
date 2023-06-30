"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .OperationalLimit import OperationalLimit


@dataclass(config=DataclassConfig)
class ActivePowerLimit(OperationalLimit):
    """
    Limit on active power flow.

    normalValue: The normal value of active power limit. The attribute shall be a positive value or zero.
    value: Value of active power limit. The attribute shall be a positive value or zero.
    """

    normalValue: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    value: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SSH,
        }
