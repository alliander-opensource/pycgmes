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
from .DynamicsFunctionBlock import DynamicsFunctionBlock


@dataclass
class DiscontinuousExcitationControlDynamics(DynamicsFunctionBlock):
    """
    Discontinuous excitation control function block whose behaviour is described by reference to a standard model or by
      definition of a user-defined model.

    RemoteInputSignal: Remote input signal used by this discontinuous excitation control system model.
    ExcitationSystemDynamics: Excitation system model with which this discontinuous excitation control model is
      associated.
    """

    # *Association not used*
    # Type M:0..1 in CIM
    # RemoteInputSignal : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    ExcitationSystemDynamics: Optional[str] = Field(
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
