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
from .WindTurbineType4IEC import WindTurbineType4IEC


@dataclass
class WindTurbineType4bIEC(WindTurbineType4IEC):
    """
    Wind turbine IEC type 4B. Reference: IEC 61400-27-1:2015, 5.5.5.3.

    WindContPType4bIEC: Wind control P type 4B model associated with this wind turbine type 4B model.
    WindGenType4IEC: Wind generator type 4 model associated with this wind turbine type 4B model.
    WindMechIEC: Wind mechanical model associated with this wind turbine type 4B model.
    """

    WindContPType4bIEC: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    WindGenType4IEC: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    WindMechIEC: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
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
            Profile.DY,
        }
