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

from ..utils.profile import BaseProfile, Profile
from .PhaseTapChanger import PhaseTapChanger


@dataclass
class PhaseTapChangerTabular(PhaseTapChanger):
    """
    Describes a tap changer with a table defining the relation between the tap step and the phase angle difference
      across the transformer.

    PhaseTapChangerTable: The phase tap changer table for this phase tap changer.
    """

    PhaseTapChangerTable: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ]
        },
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SSH,
        }
