"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .PowerSystemResource import PowerSystemResource


@dataclass
class Equipment(PowerSystemResource):
    """
    The parts of a power system that are physical devices, electronic or mechanical.

    EquipmentContainer: Container of this equipment.
    OperationalLimitSet: The operational limit sets associated with this equipment.
    aggregate: The aggregate flag provides an alternative way of representing an aggregated (equivalent) element. It is
      applicable in cases when the dedicated classes for equivalent equipment do not have all of the
      attributes necessary to represent the required level of detail.  In case the flag is set to `true`
      the single instance of equipment represents multiple pieces of equipment that have been modelled
      together as an aggregate equivalent obtained by a network reduction procedure. Examples would be
      power transformers or synchronous machines operating in parallel modelled as a single aggregate
      power transformer or aggregate synchronous machine.   The attribute is not used for
      EquivalentBranch, EquivalentShunt and EquivalentInjection.
    inService: Specifies the availability of the equipment. True means the equipment is available for topology
      processing, which determines if the equipment is energized or not. False means that the equipment
      is treated by network applications as if it is not in the model.
    normallyInService: Specifies the availability of the equipment under normal operating conditions. True means the
      equipment is available for topology processing, which determines if the equipment is
      energized or not. False means that the equipment is treated by network applications as if
      it is not in the model.
    """

    EquipmentContainer: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
                Profile.EQBD,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": True,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    OperationalLimitSet: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": False,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    aggregate: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "Boolean",
        },
    )

    inService: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.SSH,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "Boolean",
        },
    )

    normallyInService: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "namespace": "http://iec.ch/TC57/CIM100#",  # NOSONAR
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": "Boolean",
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
            Profile.DY,
            Profile.EQBD,
            Profile.SC,
            Profile.SSH,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
