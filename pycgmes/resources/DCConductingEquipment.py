"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Equipment import Equipment


@dataclass(config=DataclassConfig)
class DCConductingEquipment(Equipment):
    """
    The parts of the DC power system that are designed to carry current or that are conductively connected through DC
      terminals.

    ratedUdc: Rated DC device voltage. The attribute shall be a positive value. It is configuration data used in power
      flow.
    DCTerminals: A DC conducting equipment has DC terminals.
    """

    ratedUdc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # DCTerminals : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
