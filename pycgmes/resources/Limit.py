"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass
class Limit(IdentifiedObject):
    """
    Specifies one limit value for a Measurement. A Measurement typically has several limits that are kept together by
      the LimitSet class. The actual meaning and use of a Limit instance (i.e., if it is an alarm or warning limit
      or if it is a high or low limit) is not captured in the Limit class. However the name of a Limit instance may
      indicate both meaning and use.

    """

    # No attributes defined for this class.

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.OP
