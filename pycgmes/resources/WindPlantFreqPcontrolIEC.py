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
class WindPlantFreqPcontrolIEC(IdentifiedObject):
    """
    Frequency and active power controller model. Reference: IEC 61400-27-1:2015, Annex D.

    WindDynamicsLookupTable: The wind dynamics lookup table associated with this frequency and active power wind plant
      model.
    dprefmax: Maximum ramp rate of pWTref request from the plant controller to the wind turbines (dprefmax) (>
      WindPlantFreqPcontrolIEC.dprefmin). It is a case-dependent parameter.
    dprefmin: Minimum (negative) ramp rate of pWTref request from the plant controller to the wind turbines (dprefmin)
      (< WindPlantFreqPcontrolIEC.dprefmax). It is a project-dependent parameter.
    dpwprefmax: Maximum positive ramp rate for wind plant power reference (dpWPrefmax) (>
      WindPlantFreqPcontrolIEC.dpwprefmin). It is a project-dependent parameter.
    dpwprefmin: Maximum negative ramp rate for wind plant power reference (dpWPrefmin) (<
      WindPlantFreqPcontrolIEC.dpwprefmax). It is a project-dependent parameter.
    prefmax: Maximum pWTref request from the plant controller to the wind turbines (prefmax) (>
      WindPlantFreqPcontrolIEC.prefmin). It is a project-dependent parameter.
    prefmin: Minimum pWTref request from the plant controller to the wind turbines (prefmin) (<
      WindPlantFreqPcontrolIEC.prefmax). It is a project-dependent parameter.
    kiwpp: Plant P controller integral gain (KIWPp). It is a project-dependent parameter.
    kiwppmax: Maximum PI integrator term (KIWPpmax) (> WindPlantFreqPcontrolIEC.kiwppmin). It is a project-dependent
      parameter.
    kiwppmin: Minimum PI integrator term (KIWPpmin) (< WindPlantFreqPcontrolIEC.kiwppmax). It is a project-dependent
      parameter.
    kpwpp: Plant P controller proportional gain (KPWPp). It is a project-dependent parameter.
    kwppref: Power reference gain (KWPpref). It is a project-dependent parameter.
    tpft: Lead time constant in reference value transfer function (Tpft) (>= 0). It is a project-dependent parameter.
    tpfv: Lag time constant in reference value transfer function (Tpfv) (>= 0). It is a project-dependent parameter.
    twpffiltp: Filter time constant for frequency measurement (TWPffiltp) (>= 0). It is a project-dependent parameter.
    twppfiltp: Filter time constant for active power measurement (TWPpfiltp) (>= 0). It is a project-dependent
      parameter.
    WindPlantIEC: Wind plant model with which this wind plant frequency and active power control is associated.
    """

    # *Association not used*
    # Type M:1..n in CIM
    # WindDynamicsLookupTable : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    dprefmax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    dprefmin: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    dpwprefmax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    dpwprefmin: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    prefmax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    prefmin: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    kiwpp: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    kiwppmax: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    kiwppmin: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    kpwpp: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    kwppref: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tpft: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    tpfv: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    twpffiltp: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    twppfiltp: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ]
        },
    )

    # *Association not used*
    # Type M:1 in CIM
    # WindPlantIEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]})

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
