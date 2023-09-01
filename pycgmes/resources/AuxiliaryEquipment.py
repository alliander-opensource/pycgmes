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
from .Equipment import Equipment


@dataclass(config=DataclassConfig)
class AuxiliaryEquipment(Equipment):
    """
    AuxiliaryEquipment describe equipment that is not performing any primary functions but support for the equipment
      performing the primary function. AuxiliaryEquipment is attached to primary equipment via an association with
      Terminal.

    Terminal: The Terminal at the equipment where the AuxiliaryEquipment is attached.
    """

    Terminal: Optional[str] = Field(
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
