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
from .WindGenType3IEC import WindGenType3IEC


@dataclass
class WindGenType3bIEC(WindGenType3IEC):
    """
    IEC type 3B generator set model. Reference: IEC 61400-27-1:2015, 5.6.3.3.

    WindDynamicsLookupTable: The wind dynamics lookup table associated with this generator type 3B model.
    mwtcwp: Crowbar control mode (MWTcwp). It is a case-dependent parameter. true = 1 in the IEC model false = 0 in the
      IEC model.
    tg: Current generation time constant (Tg) (>= 0). It is a type-dependent parameter.
    two: Time constant for crowbar washout filter (Two) (>= 0). It is a case-dependent parameter.
    """

    # *Association not used*
    # Type M:1..n in CIM
    # WindDynamicsLookupTable : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    mwtcwp: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tg: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    two: int = Field(
        default=0,
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
