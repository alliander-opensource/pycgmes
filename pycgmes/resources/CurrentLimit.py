# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .OperationalLimit import OperationalLimit


@dataclass(config=DataclassConfig)
class CurrentLimit(OperationalLimit):
    """
    Operational limit on current.

    normalValue: The normal value for limit on current flow. The attribute shall be a positive value or zero.
    value: Limit on current flow. The attribute shall be a positive value or zero.
    """

    normalValue: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    value: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SSH,
        }
