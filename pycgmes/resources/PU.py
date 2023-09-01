"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class PU(Base):
    """
    Per Unit - a positive or negative value referred to a defined base. Values typically range from -10 to +10.

    value:
    unit:
    multiplier:
    """

    value: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
            Profile.SSH,
            Profile.DY,
        ],
    )

    unit: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.SC,
            Profile.SSH,
            Profile.DY,
        ],
    )

    multiplier: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.SC,
            Profile.SSH,
            Profile.DY,
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
            Profile.SSH,
            Profile.DY,
        }
