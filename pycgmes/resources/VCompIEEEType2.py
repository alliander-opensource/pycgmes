# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .VoltageCompensatorDynamics import VoltageCompensatorDynamics


@dataclass
class VCompIEEEType2(VoltageCompensatorDynamics):
    """
    Terminal voltage transducer and load compensator as defined in IEEE 421.5-2005, 4. This model is designed to cover
      the following types of compensation:   reactive droop; transformer-drop or line-drop compensation; reactive
      differential compensation known also as cross-current compensation.  Reference: IEEE 421.5-2005, 4.

    tr: Time constant which is used for the combined voltage sensing and compensation signal (Tr) (>= 0).
    GenICompensationForGenJ: Compensation of this voltage compensator`s generator for current flow out of another
      generator.
    """

    tr: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    # *Association not used*
    # Type M:2..n in CIM
    # GenICompensationForGenJ : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
