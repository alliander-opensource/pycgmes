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
from .WindTurbineType1or2IEC import WindTurbineType1or2IEC


@dataclass
class WindGenTurbineType1aIEC(WindTurbineType1or2IEC):
    """
    Wind turbine IEC type 1A. Reference: IEC 61400-27-1:2015, 5.5.2.2.

    WindAeroConstIEC: Wind aerodynamic model associated with this wind turbine type 1A model.
    """

    WindAeroConstIEC: Optional[str] = Field(
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
