"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class Date(Base):
    """
    Date as "yyyy-mm-dd", which conforms with ISO 8601. UTC time zone is specified as "yyyy-mm-ddZ". A local timezone
      relative UTC is specified as "yyyy-mm-dd(+/-)hh:mm".

    """

    # No attributes defined for this class.

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.TP,
            Profile.GL,
            Profile.DL,
            Profile.EQBD,
            Profile.EQ,
            Profile.SC,
            Profile.SV,
            Profile.SSH,
            Profile.DY,
            Profile.OP,
        }
