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
from .WindTurbineType3or4Dynamics import WindTurbineType3or4Dynamics


@dataclass(config=DataclassConfig)
class WindTurbineType3or4IEC(WindTurbineType3or4Dynamics):
    """
    Parent class supporting relationships to IEC wind turbines type 3 and type 4 including their control models.

    WindContCurrLimIEC: Wind control current limitation model associated with this wind turbine type 3 or type 4 model.
    WIndContQIEC: Wind control Q model associated with this wind turbine type 3 or type 4 model.
    WindContQLimIEC: Constant Q limitation model associated with this wind generator type 3 or type 4 model.
    WindContQPQULimIEC: QP and QU limitation model associated with this wind generator type 3 or type 4 model.
    WindProtectionIEC: Wind turbune protection model associated with this wind generator type 3 or type 4 model.
    WindRefFrameRotIEC: Reference frame rotation model associated with this wind turbine type 3 or type 4 model.
    """

    WindContCurrLimIEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WIndContQIEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindContQLimIEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindContQPQULimIEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindProtectionIEC: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    WindRefFrameRotIEC: Optional[str] = Field(
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
