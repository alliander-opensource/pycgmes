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
from .RotatingMachineDynamics import RotatingMachineDynamics


@dataclass
class AsynchronousMachineDynamics(RotatingMachineDynamics):
    """
    Asynchronous machine whose behaviour is described by reference to a standard model expressed in either time constant
      reactance form or equivalent circuit form or by definition of a user-defined model. Parameter details:
      Asynchronous machine parameters such as Xl, Xs, etc. are actually used as inductances in the model, but are
      commonly referred to as reactances since, at nominal frequency, the PU values are the same. However, some
      references use the symbol L instead of X.

    AsynchronousMachine: Asynchronous machine to which this asynchronous machine dynamics model applies.
    TurbineGovernorDynamics: Turbine-governor model associated with this asynchronous machine model.
    MechanicalLoadDynamics: Mechanical load model associated with this asynchronous machine model.
    WindTurbineType1or2Dynamics: Wind generator type 1 or type 2 model associated with this asynchronous machine model.
    """

    AsynchronousMachine: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    # *Association not used*
    # Type M:0..1 in CIM
    # TurbineGovernorDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # MechanicalLoadDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # WindTurbineType1or2Dynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
