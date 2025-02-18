"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .ACDCConverter import ACDCConverter


@dataclass
class CsConverter(ACDCConverter):
    """
    DC side of the current source converter (CSC). The firing angle controls the dc voltage at the converter, both for
      rectifier and inverter. The difference between the dc voltages of the rectifier and inverter determines the dc
      current. The extinction angle is used to limit the dc voltage at the inverter, if needed, and is not used in
      active power control. The firing angle, transformer tap position and number of connected filters are the
      primary means to control a current source dc line. Higher level controls are built on top, e.g. dc voltage, dc
      current and active power. From a steady state perspective it is sufficient to specify the wanted active power
      transfer (ACDCConverter.targetPpcc) and the control functions will set the dc voltage, dc current, firing
      angle, transformer tap position and number of connected filters to meet this. Therefore attributes targetAlpha
      and targetGamma are not applicable in this case. The reactive power consumed by the converter is a function of
      the firing angle, transformer tap position and number of connected filter, which can be approximated with half
      of the active power. The losses is a function of the dc voltage and dc current. The attributes minAlpha and
      maxAlpha define the range of firing angles for rectifier operation between which no discrete tap changer
      action takes place. The range is typically 10-18 degrees. The attributes minGamma and maxGamma define the
      range of extinction angles for inverter operation between which no discrete tap changer action takes place.
      The range is typically 17-20 degrees.

    CSCDynamics: Current source converter dynamics model used to describe dynamic behaviour of this converter.
    alpha: Firing angle that determines the dc voltage at the converter dc terminal. Typical value between 10 degrees
      and 18 degrees for a rectifier. It is converter`s state variable, result from power flow. The attribute
      shall be a positive value.
    gamma: Extinction angle. It is used to limit the dc voltage at the inverter if needed. Typical value between 17
      degrees and 20 degrees for an inverter. It is converter`s state variable, result from power flow. The
      attribute shall be a positive value.
    maxAlpha: Maximum firing angle. It is converter`s configuration data used in power flow. The attribute shall be a
      positive value.
    maxGamma: Maximum extinction angle. It is converter`s configuration data used in power flow. The attribute shall be
      a positive value.
    maxIdc: The maximum direct current (Id) on the DC side at which the converter should operate. It is converter`s
      configuration data use in power flow. The attribute shall be a positive value.
    minAlpha: Minimum firing angle. It is converter`s configuration data used in power flow. The attribute shall be a
      positive value.
    minGamma: Minimum extinction angle. It is converter`s configuration data used in power flow. The attribute shall be
      a positive value.
    minIdc: The minimum direct current (Id) on the DC side at which the converter should operate. It is converter`s
      configuration data used in power flow. The attribute shall be a positive value.
    operatingMode: Indicates whether the DC pole is operating as an inverter or as a rectifier. It is converter`s
      control variable used in power flow.
    pPccControl: Kind of active power control.
    ratedIdc: Rated converter DC current, also called IdN. The attribute shall be a positive value. It is converter`s
      configuration data used in power flow.
    targetAlpha: Target firing angle. It is converter`s control variable used in power flow. It is only applicable for
      rectifier if continuous tap changer control is used. Allowed values are within the range
      minAlpha<=targetAlpha<=maxAlpha. The attribute shall be a positive value.
    targetGamma: Target extinction angle. It is converter`s control variable used in power flow. It is only applicable
      for inverter if continuous tap changer control is used. Allowed values are within the range
      minGamma<=targetGamma<=maxGamma. The attribute shall be a positive value.
    targetIdc: DC current target value. It is converter`s control variable used in power flow. The attribute shall be a
      positive value.
    """

    CSCDynamics: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.DY,
            ],
            "is_used": False,
            "is_class_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    alpha: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SV,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    gamma: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SV,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    maxAlpha: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    maxGamma: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    maxIdc: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    minAlpha: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    minGamma: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    minIdc: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    operatingMode: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.SSH,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": True,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    pPccControl: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.SSH,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": True,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    ratedIdc: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    targetAlpha: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SSH,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    targetGamma: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SSH,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    targetIdc: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SSH,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
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
            Profile.EQ,
            Profile.SSH,
            Profile.SV,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
