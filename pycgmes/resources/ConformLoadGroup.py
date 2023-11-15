# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .LoadGroup import LoadGroup


@dataclass
class ConformLoadGroup(LoadGroup):
    """
    A group of loads conforming to an allocation pattern.

    ConformLoadSchedules: The ConformLoadSchedules in the ConformLoadGroup.
    EnergyConsumers: Conform loads assigned to this ConformLoadGroup.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # ConformLoadSchedules : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    # *Association not used*
    # Type M:1..n in CIM
    # EnergyConsumers : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
