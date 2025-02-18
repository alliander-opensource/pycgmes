"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .EquivalentEquipment import EquivalentEquipment


@dataclass
class EquivalentBranch(EquivalentEquipment):
    """
    The class represents equivalent branches. In cases where a transformer phase shift is modelled and the
      EquivalentBranch is spanning the same nodes, the impedance quantities for the EquivalentBranch shall consider
      the needed phase shift.

    negativeR12: Negative sequence series resistance from terminal sequence  1 to terminal sequence 2. Used for short
      circuit data exchange according to IEC 60909. EquivalentBranch is a result of network reduction
      prior to the data exchange.
    negativeR21: Negative sequence series resistance from terminal sequence 2 to terminal sequence 1. Used for short
      circuit data exchange according to IEC 60909. EquivalentBranch is a result of network reduction
      prior to the data exchange.
    negativeX12: Negative sequence series reactance from terminal sequence  1 to terminal sequence 2. Used for short
      circuit data exchange according to IEC 60909. Usage : EquivalentBranch is a result of network
      reduction prior to the data exchange.
    negativeX21: Negative sequence series reactance from terminal sequence 2 to terminal sequence 1. Used for short
      circuit data exchange according to IEC 60909. Usage: EquivalentBranch is a result of network
      reduction prior to the data exchange.
    positiveR12: Positive sequence series resistance from terminal sequence  1 to terminal sequence 2 . Used for short
      circuit data exchange according to IEC 60909.  EquivalentBranch is a result of network reduction
      prior to the data exchange.
    positiveR21: Positive sequence series resistance from terminal sequence 2 to terminal sequence 1. Used for short
      circuit data exchange according to IEC 60909. EquivalentBranch is a result of network reduction
      prior to the data exchange.
    positiveX12: Positive sequence series reactance from terminal sequence  1 to terminal sequence 2. Used for short
      circuit data exchange according to IEC 60909. Usage : EquivalentBranch is a result of network
      reduction prior to the data exchange.
    positiveX21: Positive sequence series reactance from terminal sequence 2 to terminal sequence 1. Used for short
      circuit data exchange according to IEC 60909. Usage : EquivalentBranch is a result of network
      reduction prior to the data exchange.
    r: Positive sequence series resistance of the reduced branch.
    r21: Resistance from terminal sequence 2 to terminal sequence 1 .Used for steady state power flow. This attribute is
      optional and represent unbalanced network such as off-nominal phase shifter. If only EquivalentBranch.r
      is given, then EquivalentBranch.r21 is assumed equal to EquivalentBranch.r. Usage rule : EquivalentBranch
      is a result of network reduction prior to the data exchange.
    x: Positive sequence series reactance of the reduced branch.
    x21: Reactance from terminal sequence 2 to terminal sequence 1. Used for steady state power flow. This attribute is
      optional and represents an unbalanced network such as off-nominal phase shifter. If only
      EquivalentBranch.x is given, then EquivalentBranch.x21 is assumed equal to EquivalentBranch.x. Usage
      rule: EquivalentBranch is a result of network reduction prior to the data exchange.
    zeroR12: Zero sequence series resistance from terminal sequence  1 to terminal sequence 2. Used for short circuit
      data exchange according to IEC 60909. EquivalentBranch is a result of network reduction prior to the
      data exchange.
    zeroR21: Zero sequence series resistance from terminal sequence  2 to terminal sequence 1. Used for short circuit
      data exchange according to IEC 60909. Usage : EquivalentBranch is a result of network reduction prior
      to the data exchange.
    zeroX12: Zero sequence series reactance from terminal sequence  1 to terminal sequence 2. Used for short circuit
      data exchange according to IEC 60909. Usage : EquivalentBranch is a result of network reduction prior
      to the data exchange.
    zeroX21: Zero sequence series reactance from terminal sequence 2 to terminal sequence 1. Used for short circuit data
      exchange according to IEC 60909. Usage : EquivalentBranch is a result of network reduction prior to
      the data exchange.
    """

    negativeR12: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    negativeR21: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    negativeX12: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    negativeX21: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    positiveR12: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    positiveR21: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    positiveX12: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    positiveX21: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    r: float = Field(
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

    r21: float = Field(
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

    x: float = Field(
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

    x21: float = Field(
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

    zeroR12: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    zeroR21: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    zeroX12: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    zeroX21: float = Field(
        default=0.0,
        json_schema_extra={
            "in_profiles": [
                Profile.SC,
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
            Profile.EQ,
            Profile.SC,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
