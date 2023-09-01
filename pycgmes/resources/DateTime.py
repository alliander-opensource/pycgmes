# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class DateTime(Base):
    """
    Date and time as "yyyy-mm-ddThh:mm:ss.sss", which conforms with ISO 8601. UTC time zone is specified as "yyyy-mm-
      ddThh:mm:ss.sssZ". A local timezone relative UTC is specified as "yyyy-mm-ddThh:mm:ss.sss-hh:mm". The second
      component (shown here as "ss.sss") could have any number of digits in its fractional part to allow any kind of
      precision beyond seconds.

    """

    # No attributes defined for this class.

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.GL,
            Profile.EQ,
            Profile.OP,
        }
