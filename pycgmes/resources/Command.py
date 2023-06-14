"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Control import Control


@dataclass(config=DataclassConfig)
class Command(Control):
    """
    A Command is a discrete control used for supervisory control.

    normalValue: Normal value for Control.value e.g. used for percentage scaling.
    value: The value representing the actuator output.
    ValueAliasSet: The ValueAliasSet used for translation of a Control value to a name.
    DiscreteValue: The MeasurementValue that is controlled.
    """

    normalValue: int = 0  # Type #Integer in CIM
    value: int = 0  # Type #Integer in CIM
    ValueAliasSet: Optional[str] = None  # Type M:0..1 in CIM
    DiscreteValue: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=Command"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "normalValue": [
                Profile.OP.value,
            ],
            "value": [
                Profile.OP.value,
            ],
            "ValueAliasSet": [
                Profile.OP.value,
            ],
            "DiscreteValue": [
                Profile.OP.value,
            ],
        }
