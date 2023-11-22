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

from ..utils.profile import BaseProfile, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass
class OperationalLimitSet(IdentifiedObject):
    """
    A set of limits associated with equipment.  Sets of limits might apply to a specific temperature, or season for
      example. A set of limits may contain different severities of limit levels that would apply to the same
      equipment. The set may contain limits of different types such as apparent power and current limits or high and
      low voltage limits  that are logically applied together as a set.

    Terminal: The terminal where the operational limit set apply.
    Equipment: The equipment to which the limit set applies.
    OperationalLimitValue: Values of equipment limits.
    """

    Terminal: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ]
        },
    )

    Equipment: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ]
        },
    )

    # *Association not used*
    # Type M:0..n in CIM
    # OperationalLimitValue : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
