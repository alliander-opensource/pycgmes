"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class TownDetail(Base):
    """
    Town details, in the context of address.

    code: Town code.
    section: Town section. For example, it is common for there to be 36 sections per township.
    name: Town name.
    stateOrProvince: Name of the state or province.
    country: Name of the country.
    """

    code: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    section: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    name: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    stateOrProvince: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    country: str = Field(
        default="",
        in_profiles=[
            Profile.GL,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.GL,
        }
