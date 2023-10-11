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
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .WindTurbineType4IEC import WindTurbineType4IEC


@dataclass(config=DataclassConfig)
class WindTurbineType4aIEC(WindTurbineType4IEC):
    """
    Wind turbine IEC type 4A. Reference: IEC 61400-27-1:2015, 5.5.5.2.

    WindContPType4aIEC: Wind control P type 4A model associated with this wind turbine type 4A model.
    WindGenType4IEC: Wind generator type 4 model associated with this wind turbine type 4A model.
    """

    WindContPType4aIEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindGenType4IEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
