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

from ..utils.base import Base
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile


@dataclass(config=DataclassConfig)
class NonlinearShuntCompensatorPoint(Base):
    """
    A non linear shunt compensator bank or section admittance value. The number of NonlinearShuntCompenstorPoint
      instances associated with a NonlinearShuntCompensator shall be equal to ShuntCompensator.maximumSections.
      ShuntCompensator.sections shall only be set to one of the NonlinearShuntCompenstorPoint.sectionNumber. There
      is no interpolation between NonlinearShuntCompenstorPoint-s.

    NonlinearShuntCompensator: Non-linear shunt compensator owning this point.
    b: Positive sequence shunt (charging) susceptance per section.
    g: Positive sequence shunt (charging) conductance per section.
    sectionNumber: The number of the section.
    b0: Zero sequence shunt (charging) susceptance per section.
    g0: Zero sequence shunt (charging) conductance per section.
    """

    NonlinearShuntCompensator: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    b: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    g: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    sectionNumber: int = Field(
        default=0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    b0: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    g0: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SC,
        }
