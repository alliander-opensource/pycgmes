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
from .IdentifiedObject import IdentifiedObject


@dataclass
class WindRefFrameRotIEC(IdentifiedObject):
    """
    Reference frame rotation model. Reference: IEC 61400-27-1:2015, 5.6.3.5.

    tpll: Time constant for PLL first order filter model (TPLL) (>= 0). It is a type-dependent parameter.
    upll1: Voltage below which the angle of the voltage is filtered and possibly also frozen (uPLL1). It is a type-
      dependent parameter.
    upll2: Voltage (uPLL2) below which the angle of the voltage is frozen if uPLL2 is smaller or equal to uPLL1 . It is
      a type-dependent parameter.
    WindTurbineType3or4IEC: Wind turbine type 3 or type 4 model with which this reference frame rotation model is
      associated.
    """

    tpll: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    upll1: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    upll2: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    # *Association not used*
    # Type M:1 in CIM
    # WindTurbineType3or4IEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
