"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ShuntCompensator import ShuntCompensator


@dataclass(config=DataclassConfig)
class LinearShuntCompensator(ShuntCompensator):
    """
    A linear shunt compensator has banks or sections with equal admittance values.

    bPerSection: Positive sequence shunt (charging) susceptance per section.
    gPerSection: Positive sequence shunt (charging) conductance per section.
    b0PerSection: Zero sequence shunt (charging) susceptance per section.
    g0PerSection: Zero sequence shunt (charging) conductance per section.
    """

    bPerSection: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    gPerSection: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    b0PerSection: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    g0PerSection: float = Field(
        default=0.0,
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
            Profile.EQ,
            Profile.SC,
            Profile.SSH,
        }
