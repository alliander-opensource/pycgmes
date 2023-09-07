# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .MechanicalLoadDynamics import MechanicalLoadDynamics


@dataclass(config=DataclassConfig)
class MechLoad1(MechanicalLoadDynamics):
    """
    Mechanical load model type 1.

    a: Speed squared coefficient (a).
    b: Speed coefficient (b).
    d: Speed to the exponent coefficient (d).
    e: Exponent (e).
    """

    a: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    b: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    d: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    e: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
