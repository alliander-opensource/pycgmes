"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .LimitSet import LimitSet


@dataclass(config=DataclassConfig)
class AnalogLimitSet(LimitSet):
    """
    An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement.

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
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # Limits : list = Field(default_factory=list, in_profiles = [Profile.OP, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }
