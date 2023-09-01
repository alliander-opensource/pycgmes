"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IOPoint import IOPoint


@dataclass(config=DataclassConfig)
class Control(IOPoint):
    """
    Control is used for supervisory/device control. It represents control outputs that are used to change the state in a
      process, e.g. close or open breaker, a set point value or a raise lower command.

    controlType: Specifies the type of Control. For example, this specifies if the Control represents BreakerOpen,
      BreakerClose, GeneratorVoltageSetPoint, GeneratorRaise, GeneratorLower, etc.
    operationInProgress: Indicates that a client is currently sending control commands that has not completed.
    timeStamp: The last time a control output was sent.
    unitMultiplier: The unit multiplier of the controlled quantity.
    unitSymbol: The unit of measure of the controlled quantity.
    PowerSystemResource: Regulating device governed by this control output.
    """

    controlType: str = Field(
        default="",
        in_profiles=[
            Profile.OP,
        ],
    )

    operationInProgress: bool = Field(
        default=False,
        in_profiles=[
            Profile.OP,
        ],
    )

    timeStamp: str = Field(
        default="",
        in_profiles=[
            Profile.OP,
        ],
    )

    unitMultiplier: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.OP,
        ],
    )

    unitSymbol: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.OP,
        ],
    )

    PowerSystemResource: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.OP,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.OP,
        }
