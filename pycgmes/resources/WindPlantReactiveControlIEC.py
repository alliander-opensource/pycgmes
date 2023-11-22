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
from .IdentifiedObject import IdentifiedObject


@dataclass
class WindPlantReactiveControlIEC(IdentifiedObject):
    """
    Simplified plant voltage and reactive power control model for use with type 3 and type 4 wind turbine models.
      Reference: IEC 61400-27-1:2015, Annex D.

    WindDynamicsLookupTable: The wind dynamics lookup table associated with this voltage and reactive power wind plant
      model.
    WindPlantIEC: Wind plant reactive control model associated with this wind plant.
    dxrefmax: Maximum positive ramp rate for wind turbine reactive power/voltage reference (dxrefmax) (>
      WindPlantReactiveControlIEC.dxrefmin). It is a project-dependent parameter.
    dxrefmin: Maximum negative ramp rate for wind turbine reactive power/voltage reference (dxrefmin) (<
      WindPlantReactiveControlIEC.dxrefmax). It is a project-dependent parameter.
    kiwpx: Plant Q controller integral gain (KIWPx). It is a project-dependent parameter.
    kiwpxmax: Maximum reactive power/voltage reference from integration (KIWPxmax) (>
      WindPlantReactiveControlIEC.kiwpxmin). It is a project-dependent parameter.
    kiwpxmin: Minimum reactive power/voltage reference from integration (KIWPxmin) (<
      WindPlantReactiveControlIEC.kiwpxmax). It is a project-dependent parameter.
    kpwpx: Plant Q controller proportional gain (KPWPx). It is a project-dependent parameter.
    kwpqref: Reactive power reference gain (KWPqref). It is a project-dependent parameter.
    kwpqu: Plant voltage control droop (KWPqu). It is a project-dependent parameter.
    tuqfilt: Filter time constant for voltage-dependent reactive power (Tuqfilt) (>= 0). It is a project-dependent
      parameter.
    twppfiltq: Filter time constant for active power measurement (TWPpfiltq) (>= 0). It is a project-dependent
      parameter.
    twpqfiltq: Filter time constant for reactive power measurement (TWPqfiltq) (>= 0). It is a project-dependent
      parameter.
    twpufiltq: Filter time constant for voltage measurement (TWPufiltq) (>= 0). It is a project-dependent parameter.
    txft: Lead time constant in reference value transfer function (Txft) (>= 0). It is a project-dependent parameter.
    txfv: Lag time constant in reference value transfer function (Txfv) (>= 0). It is a project-dependent parameter.
    uwpqdip: Voltage threshold for UVRT detection in Q control (uWPqdip). It is a project-dependent parameter.
    windPlantQcontrolModesType: Reactive power/voltage controller mode (MWPqmode). It is a case-dependent parameter.
    xrefmax: Maximum xWTref (qWTref or delta uWTref) request from the plant controller (xrefmax) (>
      WindPlantReactiveControlIEC.xrefmin). It is a case-dependent parameter.
    xrefmin: Minimum xWTref (qWTref or delta uWTref) request from the plant controller (xrefmin) (<
      WindPlantReactiveControlIEC.xrefmax). It is a project-dependent parameter.
    """

    # *Association not used*
    # Type M:1..n in CIM
    # WindDynamicsLookupTable : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:1 in CIM
    # WindPlantIEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]})

    dxrefmax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    dxrefmin: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    kiwpx: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    kiwpxmax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    kiwpxmin: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    kpwpx: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    kwpqref: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    kwpqu: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tuqfilt: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    twppfiltq: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    twpqfiltq: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    twpufiltq: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    txft: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    txfv: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    uwpqdip: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    windPlantQcontrolModesType: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    xrefmax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    xrefmin: float = Field(
        default=0.0,
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
