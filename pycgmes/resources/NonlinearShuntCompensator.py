"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ShuntCompensator import ShuntCompensator


@dataclass(config=DataclassConfig)
class NonlinearShuntCompensator(ShuntCompensator):
    """
    A non linear shunt compensator has bank or section admittance values that differ. The attributes g, b, g0 and b0 of
      the associated NonlinearShuntCompensatorPoint describe the total conductance and admittance of a
      NonlinearShuntCompensatorPoint at a section number specified by NonlinearShuntCompensatorPoint.sectionNumber.

    NonlinearShuntCompensatorPoints: All points of the non-linear shunt compensator.
    """

    # *Association not used*
    # Type M:1..n in CIM  # pylint: disable-next=line-too-long
    # NonlinearShuntCompensatorPoints : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

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
