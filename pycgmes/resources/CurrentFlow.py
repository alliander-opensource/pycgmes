# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

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
class CurrentFlow(Base):
    """
    Electrical current with sign convention: positive flow is out of the conducting equipment into the connectivity
      node. Can be both AC and DC.

    value:
    multiplier:
    unit:
    """

    value: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
            Profile.SC,
            Profile.SV,
            Profile.SSH,
        ],
    )

    multiplier: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
            Profile.SC,
            Profile.SV,
            Profile.SSH,
        ],
    )

    unit: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
            Profile.SC,
            Profile.SV,
            Profile.SSH,
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
            Profile.SV,
            Profile.SSH,
        }
