"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Connector import Connector


@dataclass(config=DataclassConfig)
class Junction(Connector):
    """
    A point where one or more conducting equipments are connected with zero resistance.

    """

    # No attributes defined for this class.

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQBD,
            Profile.EQ,
        }
