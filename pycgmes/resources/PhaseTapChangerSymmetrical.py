# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PhaseTapChangerNonLinear import PhaseTapChangerNonLinear


@dataclass(config=DataclassConfig)
class PhaseTapChangerSymmetrical(PhaseTapChangerNonLinear):
    """
    Describes a symmetrical phase shifting transformer tap model in which the voltage magnitude of both sides is the
      same. The difference voltage magnitude is the base in an equal-sided triangle where the sides corresponds to
      the primary and secondary voltages. The phase angle difference corresponds to the top angle and can be
      expressed as twice the arctangent of half the total difference voltage.

    """

    # No attributes defined for this class.

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SSH,
        }
