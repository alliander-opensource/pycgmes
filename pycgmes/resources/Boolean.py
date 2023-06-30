"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class Boolean(Base):
    """
    A type with the value space "true" and "false".

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
            Profile.DL,
            Profile.EQBD,
            Profile.EQ,
            Profile.SC,
            Profile.SV,
            Profile.SSH,
            Profile.DY,
            Profile.OP,
        }
