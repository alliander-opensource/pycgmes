# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class ControlAreaGeneratingUnit(IdentifiedObject):
    """
    A control area generating unit. This class is needed so that alternate control area definitions may include the same
      generating unit.   It should be noted that only one instance within a control area should reference a specific
      generating unit.

    ControlArea: The parent control area for the generating unit specifications.
    GeneratingUnit: The generating unit specified for this control area.  Note that a control area should include a
      GeneratingUnit only once.
    """

    ControlArea: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    GeneratingUnit: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
