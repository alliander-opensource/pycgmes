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
from .Base import Base


@dataclass(config=DataclassConfig)
class SvVoltage(Base):
    """
    State variable for voltage.

    angle: The voltage angle of the topological node complex voltage with respect to system reference.
    v: The voltage magnitude at the topological node. The attribute shall be a positive value.
    TopologicalNode: The topological node associated with the voltage state.
    """

    angle: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SV,
        ],
    )

    v: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SV,
        ],
    )

    TopologicalNode: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.SV,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.SV,
        }
