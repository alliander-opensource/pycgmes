"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .EquipmentContainer import EquipmentContainer


@dataclass
class VoltageLevel(EquipmentContainer):
    """
    A collection of equipment at one common system voltage forming a switchgear. The equipment typically consists of
      breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all
      these.

    BaseVoltage: The base voltage used for all equipment within the voltage level.
    Bays: The bays within this voltage level.
    Substation: The substation of the voltage level.
    highVoltageLimit: The bus bar`s high voltage limit. The limit applies to all equipment and nodes contained in a
      given VoltageLevel. It is not required that it is exchanged in pair with lowVoltageLimit. It
      is preferable to use operational VoltageLimit, which prevails, if present.
    lowVoltageLimit: The bus bar`s low voltage limit. The limit applies to all equipment and nodes contained in a given
      VoltageLevel. It is not required that it is exchanged in pair with highVoltageLimit. It is
      preferable to use operational VoltageLimit, which prevails, if present.
    """

    BaseVoltage: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
                Profile.EQBD,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    Bays: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
                Profile.EQBD,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    Substation: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
                Profile.EQBD,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    highVoltageLimit: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
                Profile.EQBD,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "Voltage",
        },
    )

    lowVoltageLimit: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
                Profile.EQBD,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": "Voltage",
        },
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.EQBD,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
