"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .MeasurementValue import MeasurementValue


@dataclass(config=DataclassConfig)
class DiscreteValue(MeasurementValue):
    """
    DiscreteValue represents a discrete MeasurementValue.

    Command: The Control variable associated with the MeasurementValue.
    Discrete: Measurement to which this value is connected.
    """

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # Command : Optional[str] = Field(default=None, in_profiles = [Profile.OP, ])

    Discrete: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.OP,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }
