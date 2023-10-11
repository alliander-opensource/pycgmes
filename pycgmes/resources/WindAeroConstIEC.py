# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class WindAeroConstIEC(IdentifiedObject):
    """
    Constant aerodynamic torque model which assumes that the aerodynamic torque is constant. Reference: IEC
      61400-27-1:2015, 5.6.1.1.

    WindGenTurbineType1aIEC: Wind turbine type 1A model with which this wind aerodynamic model is associated.
    """

    # *Association not used*
    # Type M:1 in CIM  # pylint: disable-next=line-too-long
    # WindGenTurbineType1aIEC : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
