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
class WindGenType3aIEC(WindGenType3IEC):
    """
    IEC type 3A generator set model. Reference: IEC 61400-27-1:2015, 5.6.3.2.

    kpc: Current PI controller proportional gain (KPc). It is a type-dependent parameter.
    tic: Current PI controller integration time constant (TIc) (>= 0). It is a type-dependent parameter.
    WindTurbineType4IEC: Wind turbine type 4 model with which this wind generator type 3A model is associated.
    """

    kpc: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tic: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    # *Association not used*
    # Type M:0..1 in CIM
    # WindTurbineType4IEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
