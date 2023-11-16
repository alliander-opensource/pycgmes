# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindContQLimIEC(IdentifiedObject):
    """
    Constant Q limitation model. Reference: IEC 61400-27-1:2015, 5.6.5.9.

    qmax: Maximum reactive power (qmax) (> WindContQLimIEC.qmin). It is a type-dependent parameter.
    qmin: Minimum reactive power (qmin) (< WindContQLimIEC.qmax). It is a type-dependent parameter.
    WindTurbineType3or4IEC: Wind generator type 3 or type 4 model with which this constant Q limitation model is
      associated.
    """

    qmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    qmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # WindTurbineType3or4IEC : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
