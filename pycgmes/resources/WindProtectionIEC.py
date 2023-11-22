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
class WindProtectionIEC(IdentifiedObject):
    """
    The grid protection model includes protection against over- and under-voltage, and against over- and under-
      frequency. Reference: IEC 61400-27-1:2015, 5.6.6.

    WindDynamicsLookupTable: The wind dynamics lookup table associated with this grid protection model.
    dfimax: Maximum rate of change of frequency (dFmax). It is a type-dependent parameter.
    fover: Wind turbine over frequency protection activation threshold (fover). It is a project-dependent parameter.
    funder: Wind turbine under frequency protection activation threshold (funder). It is a project-dependent parameter.
    mzc: Zero crossing measurement mode (Mzc).  It is a type-dependent parameter.  true = WT protection system uses zero
      crossings to detect frequency (1 in the IEC model) false = WT protection system does not use zero
      crossings to detect frequency (0 in the IEC model).
    tfma: Time interval of moving average window (TfMA) (>= 0).  It is a type-dependent parameter.
    uover: Wind turbine over voltage protection activation threshold (uover). It is a project-dependent parameter.
    uunder: Wind turbine under voltage protection activation threshold (uunder). It is a project-dependent parameter.
    WindTurbineType3or4IEC: Wind generator type 3 or type 4 model with which this wind turbine protection model is
      associated.
    WindTurbineType1or2IEC: Wind generator type 1 or type 2 model with which this wind turbine protection model is
      associated.
    """

    # *Association not used*
    # Type M:1..n in CIM
    # WindDynamicsLookupTable : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    dfimax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    fover: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    funder: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    mzc: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tfma: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    uover: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    uunder: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    # *Association not used*
    # Type M:0..1 in CIM
    # WindTurbineType3or4IEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # WindTurbineType1or2IEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
