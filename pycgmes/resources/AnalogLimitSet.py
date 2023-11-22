# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .LimitSet import LimitSet


@dataclass
class AnalogLimitSet(LimitSet):
    """
    An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement.

    Measurements: The Measurements using the LimitSet.
    Limits: The limit values used for supervision of Measurements.
    """

    Measurements: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ]
        },
    )

    # *Association not used*
    # Type M:0..n in CIM
    # Limits : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.OP, ]})

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }
