"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from ..utils.base import Base


@dataclass
class UnitMultiplier(Base):
    """
    The unit multipliers defined for the CIM.  When applied to unit symbols, the unit symbol is treated as a derived
      unit. Regardless of the contents of the unit symbol text, the unit symbol shall be treated as if it were a
      single-character unit symbol. Unit symbols should not contain multipliers, and it should be left to the
      multiplier to define the multiple for an entire data type.   For example, if a unit symbol is "m2Pers" and the
      multiplier is "k", then the value is k(m**2/s), and the multiplier applies to the entire final value, not to
      any individual part of the value. This can be conceptualized by substituting a derived unit symbol for the
      unit type. If one imagines that the symbol "Þ" represents the derived unit "m2Pers", then applying the
      multiplier "k" can be conceptualized simply as "kÞ".  For example, the SI unit for mass is "kg" and not "g".
      If the unit symbol is defined as "kg", then the multiplier is applied to "kg" as a whole and does not replace
      the "k" in front of the "g". In this case, the multiplier of "m" would be used with the unit symbol of "kg" to
      represent one gram.  As a text string, this violates the instructions in IEC 80000-1. However, because the
      unit symbol in CIM is treated as a derived unit instead of as an SI unit, it makes more sense to conceptualize
      the "kg" as if it were replaced by one of the proposed replacements for the SI mass symbol. If one imagines
      that the "kg" were replaced by a symbol "Þ", then it is easier to conceptualize the multiplier "m" as creating
      the proper unit "mÞ", and not the forbidden unit "mkg".

    """

    # No attributes defined for this class.

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DL,
            Profile.DY,
            Profile.EQ,
            Profile.EQBD,
            Profile.OP,
            Profile.SC,
            Profile.SSH,
            Profile.SV,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
