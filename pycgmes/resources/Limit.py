"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class Limit(IdentifiedObject):
    """
    Specifies one limit value for a Measurement. A Measurement typically has several limits that are kept together by
      the LimitSet class. The actual meaning and use of a Limit instance (i.e., if it is an alarm or warning limit
      or if it is a high or low limit) is not captured in the Limit class. However the name of a Limit instance may
      indicate both meaning and use.

    """

    # No attributes defined for this class.

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }
