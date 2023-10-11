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

from .DynamicsFunctionBlock import DynamicsFunctionBlock


@dataclass(config=DataclassConfig)
class WindTurbineType1or2Dynamics(DynamicsFunctionBlock):
    """
    Parent class supporting relationships to wind turbines type 1 and type 2 and their control models.  Generator model
      for wind turbine of type 1 or type 2 is a standard asynchronous generator model.

    RemoteInputSignal: Remote input signal used by this wind generator type 1 or type 2 model.
    AsynchronousMachineDynamics: Asynchronous machine model with which this wind generator type 1 or type 2 model is
      associated.
    """

    RemoteInputSignal: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    AsynchronousMachineDynamics: Optional[str] = Field(
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
