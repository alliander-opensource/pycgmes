"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .ConductingEquipment import ConductingEquipment
from .Boolean import Boolean
from .CurrentFlow import CurrentFlow


@dataclass
class Switch(ConductingEquipment):
    """
    A generic device designed to close, or open, or both, one or more electric circuits.  All switches are two terminal
      devices including grounding switches. The ACDCTerminal.connected at the two sides of the switch shall not be
      considered for assessing switch connectivity, i.e. only Switch.open, .normalOpen and .locked are relevant.

    SvSwitch: The switch state associated with the switch.
    SwitchSchedules: A Switch can be associated with SwitchSchedules.
    locked: If true, the switch is locked. The resulting switch state is a combination of locked and Switch.open
      attributes as follows:  locked=true and Switch.open=true. The resulting state is open and locked;
      locked=false and Switch.open=true. The resulting state is open; locked=false and Switch.open=false.
      The resulting state is closed.
    normalOpen: The attribute is used in cases when no Measurement for the status value is present. If the Switch has a
      status measurement the Discrete.normalValue is expected to match with the Switch.normalOpen.
    open: The attribute tells if the switch is considered open when used as input to topology processing.
    ratedCurrent: The maximum continuous current carrying capacity in amps governed by the device material and
      construction. The attribute shall be a positive value.
    retained: Branch is retained in the topological solution.  The flow through retained switches will normally be
      calculated in power flow.
    """

    SvSwitch: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.SV,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    SwitchSchedules: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    locked: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.SSH,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": Boolean,
        },
    )

    normalOpen: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": Boolean,
        },
    )

    open: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.SSH,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": Boolean,
        },
    )

    ratedCurrent: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
            "attribute_class": CurrentFlow,
        },
    )

    retained: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_datatype_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
            "attribute_class": Boolean,
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
