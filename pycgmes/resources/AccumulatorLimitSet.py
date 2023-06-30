"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .LimitSet import LimitSet


@dataclass(config=DataclassConfig)
class AccumulatorLimitSet(LimitSet):
    """
    An AccumulatorLimitSet specifies a set of Limits that are associated with an Accumulator measurement.

    Measurements: The Measurements using the LimitSet.
    Limits: The limit values used for supervision of Measurements.
    """

    Measurements: list = Field(
        default_factory=list,
        in_profiles=[
            Profile.OP,
        ],
    )

    # *Association not used*
    # Type M:1..n in CIM  # pylint: disable-next=line-too-long
    # Limits : list = Field(default_factory=list, in_profiles = [Profile.OP, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }
