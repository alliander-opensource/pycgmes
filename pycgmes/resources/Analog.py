"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Measurement import Measurement


@dataclass(config=DataclassConfig)
class Analog(Measurement):
    """
    Analog represents an analog Measurement.

    positiveFlowIn: If true then this measurement is an active power, reactive power or current with the convention that
      a positive value measured at the Terminal means power is flowing into the related
      PowerSystemResource.
    AnalogValues: The values connected to this measurement.
    LimitSets: A measurement may have zero or more limit ranges defined for it.
    """

    positiveFlowIn: bool = Field(
        default=False,
        in_profiles=[
            Profile.OP,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # AnalogValues : list = Field(default_factory=list, in_profiles = [Profile.OP, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # LimitSets : list = Field(default_factory=list, in_profiles = [Profile.OP, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }
