"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class PerCent(Base):
    """
    Percentage on a defined base.   For example, specify as 100 to indicate at the defined base.

    value: Normally 0 to 100 on a defined base.
    unit:
    multiplier:
    """

    value: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
            Profile.SC,
            Profile.SSH,
            Profile.OP,
        ],
    )

    unit: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
            Profile.SC,
            Profile.SSH,
            Profile.OP,
        ],
    )

    multiplier: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
            Profile.SC,
            Profile.SSH,
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
            Profile.EQ,
            Profile.SC,
            Profile.SSH,
            Profile.OP,
        }
