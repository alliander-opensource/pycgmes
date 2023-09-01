"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .TapChangerTablePoint import TapChangerTablePoint


@dataclass(config=DataclassConfig)
class RatioTapChangerTablePoint(TapChangerTablePoint):
    """
    Describes each tap step in the ratio tap changer tabular curve.

    RatioTapChangerTable: Table of this point.
    """

    RatioTapChangerTable: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
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
        }
