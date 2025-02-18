"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .RegulatingCondEq import RegulatingCondEq


@dataclass
class StaticVarCompensator(RegulatingCondEq):
    """
    A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown
      transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate
      in fixed MVar output mode or in voltage control mode. When in voltage control mode, the output of the SVC will
      be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC
      characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage
      setpoint, the SVC MVar output is zero.

    StaticVarCompensatorDynamics: Static Var Compensator dynamics model used to describe dynamic behaviour of this
      Static Var Compensator.
    capacitiveRating: Capacitive reactance at maximum capacitive reactive power.  Shall always be positive.
    inductiveRating: Inductive reactance at maximum inductive reactive power.  Shall always be negative.
    q: Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting
      value for a steady state solution.
    sVCControlMode: SVC control mode.
    slope: The characteristics slope of an SVC defines how the reactive power output changes in proportion to the
      difference between the regulated bus voltage and the voltage setpoint. The attribute shall be a
      positive value or zero.
    voltageSetPoint: The reactive power output of the SVC is proportional to the difference between the voltage at the
      regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the
      voltage setpoint, the reactive power output is zero.
    """

    StaticVarCompensatorDynamics: Optional[str] = Field(
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

    capacitiveRating: float = Field(
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

    inductiveRating: float = Field(
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

    q: float = Field(
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

    sVCControlMode: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": True,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    slope: float = Field(
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

    voltageSetPoint: float = Field(
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
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
