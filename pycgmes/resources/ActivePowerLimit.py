"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .OperationalLimit import OperationalLimit


@dataclass(config=DataclassConfig)
class ActivePowerLimit(OperationalLimit):
    """
    Limit on active power flow.

    normalValue: The normal value of active power limit. The attribute shall be a positive value or zero.
    value: Value of active power limit. The attribute shall be a positive value or zero.
    """

    normalValue: float = 0.0  # Type #ActivePower in CIM
    value: float = 0.0  # Type #ActivePower in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ActivePowerLimit"]
            + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.EQ.value,
                Profile.SSH.value,
            ],
            # Attributes
            "normalValue": [
                Profile.EQ.value,
            ],
            "value": [
                Profile.SSH.value,
            ],
        }
