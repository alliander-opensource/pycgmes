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
class WindContCurrLimIEC(IdentifiedObject):
    """
    Current limitation model.  The current limitation model combines the physical limits and the control limits.
      Reference: IEC 61400-27-1:2015, 5.6.5.8.

    imax: Maximum continuous current at the wind turbine terminals (imax). It is a type-dependent parameter.
    imaxdip: Maximum current during voltage dip at the wind turbine terminals (imaxdip). It is a project-dependent
      parameter.
    kpqu: Partial derivative of reactive current limit (Kpqu) versus voltage. It is a type-dependent parameter.
    mdfslim: Limitation of type 3 stator current (MDFSLim). MDFSLim = 1 for wind turbines type 4. It is a type-dependent
      parameter. false= total current limitation (0 in the IEC model) true=stator current limitation (1 in
      the IEC model).
    mqpri: Prioritisation of Q control during UVRT (Mqpri). It is a project-dependent parameter. true = reactive power
      priority (1 in the IEC model) false = active power priority (0 in the IEC model).
    tufiltcl: Voltage measurement filter time constant (Tufiltcl) (>= 0). It is a type-dependent parameter.
    upqumax: Wind turbine voltage in the operation point where zero reactive current can be delivered (upqumax). It is a
      type-dependent parameter.
    WindTurbineType3or4IEC: Wind turbine type 3 or type 4 model with which this wind control current limitation model is
      associated.
    WindDynamicsLookupTable: The wind dynamics lookup table associated with this current control limitation model.
    """

    imax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    imaxdip: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    kpqu: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    mdfslim: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    mqpri: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tufiltcl: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    upqumax: float = Field(
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

    # *Association not used*
    # Type M:1..n in CIM
    # WindDynamicsLookupTable : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
