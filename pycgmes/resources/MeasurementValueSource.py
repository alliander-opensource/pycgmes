# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass
class MeasurementValueSource(IdentifiedObject):
    """
    MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to
      use the MeasurementValueSource attributes are defined in IEC 61970-301.

    MeasurementValues: The MeasurementValues updated by the source.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # MeasurementValues : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.OP, ]}) # noqa: E501

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }
