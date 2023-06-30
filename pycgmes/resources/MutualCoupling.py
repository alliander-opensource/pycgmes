"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class MutualCoupling(IdentifiedObject):
    """
    This class represents the zero sequence line mutual coupling.

    b0ch: Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section.
    distance11: Distance to the start of the coupled region from the first line`s terminal having sequence number equal
      to 1.
    distance12: Distance to the end of the coupled region from the first line`s terminal with sequence number equal to
      1.
    distance21: Distance to the start of coupled region from the second line`s terminal with sequence number equal to 1.
    distance22: Distance to the end of coupled region from the second line`s terminal with sequence number equal to 1.
    g0ch: Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section.
    r0: Zero sequence branch-to-branch mutual impedance coupling, resistance.
    x0: Zero sequence branch-to-branch mutual impedance coupling, reactance.
    Second_Terminal: The starting terminal for the calculation of distances along the second branch of the mutual
      coupling.
    First_Terminal: The starting terminal for the calculation of distances along the first branch of the mutual
      coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The
      first and second terminals of a mutual coupling should point to different AC line segments.
    """

    b0ch: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    distance11: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    distance12: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    distance21: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    distance22: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    g0ch: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    r0: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    x0: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    Second_Terminal: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.SC,
        ],
    )

    First_Terminal: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.SC,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.SC,
        }
