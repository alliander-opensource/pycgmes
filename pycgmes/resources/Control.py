"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
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

    controlType: str = ""  # Type #String in CIM
    operationInProgress: bool = False  # Type #Boolean in CIM
    timeStamp: str = ""  # Type #DateTime in CIM
    unitMultiplier: Optional[str] = None  # Type M:0..1 in CIM
    unitSymbol: Optional[str] = None  # Type M:0..1 in CIM
    PowerSystemResource: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=Control"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
        )

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                Profile.OP.value,
            ],
            # Attributes
            "controlType": [
                Profile.OP.value,
            ],
            "operationInProgress": [
                Profile.OP.value,
            ],
            "timeStamp": [
                Profile.OP.value,
            ],
            "unitMultiplier": [
                Profile.OP.value,
            ],
            "unitSymbol": [
                Profile.OP.value,
            ],
            "PowerSystemResource": [
                Profile.OP.value,
            ],
        }
