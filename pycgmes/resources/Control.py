"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .IOPoint import IOPoint


@dataclass
class Control(IOPoint):
    """
    Control is used for supervisory/device control. It represents control outputs that are used to change the state in a
      process, e.g. close or open breaker, a set point value or a raise lower command.

    PowerSystemResource: Regulating device governed by this control output.
    controlType: Specifies the type of Control. For example, this specifies if the Control represents BreakerOpen,
      BreakerClose, GeneratorVoltageSetPoint, GeneratorRaise, GeneratorLower, etc.
    operationInProgress: Indicates that a client is currently sending control commands that has not completed.
    timeStamp: The last time a control output was sent.
    unitMultiplier: The unit multiplier of the controlled quantity.
    unitSymbol: The unit of measure of the controlled quantity.
    """

    PowerSystemResource: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    controlType: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    operationInProgress: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    timeStamp: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    unitMultiplier: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": True,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    unitSymbol: str = Field(
        default="",
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": True,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.OP
