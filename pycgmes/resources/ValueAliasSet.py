# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class ValueAliasSet(IdentifiedObject):
    """
    Describes the translation of a set of values into a name and is intendend to facilitate custom translations. Each
      ValueAliasSet has a name, description etc. A specific Measurement may represent a discrete state like Open,
      Closed, Intermediate etc. This requires a translation from the MeasurementValue.value number to a string, e.g.
      0->"Invalid", 1->"Open", 2->"Closed", 3->"Intermediate". Each ValueToAlias member in ValueAliasSet.Value
      describe a mapping for one particular value to a name.

    Commands: The Commands using the set for translation.
    Discretes: The Measurements using the set for translation.
    RaiseLowerCommands: The Commands using the set for translation.
    Values: The ValueToAlias mappings included in the set.
    """

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # Commands : list = Field(default_factory=list, in_profiles = [Profile.OP, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # Discretes : list = Field(default_factory=list, in_profiles = [Profile.OP, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # RaiseLowerCommands : list = Field(default_factory=list, in_profiles = [Profile.OP, ])

    # *Association not used*
    # Type M:1..n in CIM  # pylint: disable-next=line-too-long
    # Values : list = Field(default_factory=list, in_profiles = [Profile.OP, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }
