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
class ExcitationSystemDynamics(DynamicsFunctionBlock):
    """
    Excitation system function block whose behaviour is described by reference to a standard model or by definition of a
      user-defined model.

    SynchronousMachineDynamics: Synchronous machine model with which this excitation system model is associated.
    VoltageCompensatorDynamics: Voltage compensator model associated with this excitation system model.
    OverexcitationLimiterDynamics: Overexcitation limiter model associated with this excitation system model.
    PFVArControllerType2Dynamics: Power factor or VAr controller type 2 model associated with this excitation system
      model.
    DiscontinuousExcitationControlDynamics: Discontinuous excitation control model associated with this excitation
      system model.
    PowerSystemStabilizerDynamics: Power system stabilizer model associated with this excitation system model.
    UnderexcitationLimiterDynamics: Undrexcitation limiter model associated with this excitation system model.
    PFVArControllerType1Dynamics: Power factor or VAr controller type 1 model associated with this excitation system
      model.
    """

    SynchronousMachineDynamics: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    # *Association not used*
    # Type M:1 in CIM
    # VoltageCompensatorDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # OverexcitationLimiterDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # PFVArControllerType2Dynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # DiscontinuousExcitationControlDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # PowerSystemStabilizerDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # UnderexcitationLimiterDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # PFVArControllerType1Dynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
