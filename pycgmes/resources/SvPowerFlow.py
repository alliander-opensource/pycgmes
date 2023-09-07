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
class SvPowerFlow(Base):
    """
    State variable for power flow. Load convention is used for flow direction. This means flow out from the
      TopologicalNode into the equipment is positive.

    p: The active power flow. Load sign convention is used, i.e. positive sign means flow out from a TopologicalNode
      (bus) into the conducting equipment.
    q: The reactive power flow. Load sign convention is used, i.e. positive sign means flow out from a TopologicalNode
      (bus) into the conducting equipment.
    Terminal: The terminal associated with the power flow state variable.
    """

    p: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SV,
        ],
    )

    q: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SV,
        ],
    )

    Terminal: Optional[str] = Field(
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
