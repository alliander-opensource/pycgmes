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
class OperationalLimit(IdentifiedObject):
    """
    A value and normal value associated with a specific kind of limit.  The sub class value and normalValue attributes
      vary inversely to the associated OperationalLimitType.acceptableDuration (acceptableDuration for short).   If
      a particular piece of equipment has multiple operational limits of the same kind (apparent power, current,
      etc.), the limit with the greatest acceptableDuration shall have the smallest limit value and the limit with
      the smallest acceptableDuration shall have the largest limit value.  Note: A large current can only be allowed
      to flow through a piece of equipment for a short duration without causing damage, but a lesser current can be
      allowed to flow for a longer duration.

    OperationalLimitSet: The limit set to which the limit values belong.
    OperationalLimitType: The limit type associated with this limit.
    """

    OperationalLimitSet: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ]
        },
    )

    OperationalLimitType: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ]
        },
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
