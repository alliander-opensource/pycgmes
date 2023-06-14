"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .OperationalLimit import OperationalLimit


@dataclass(config=DataclassConfig)
class VoltageLimit(OperationalLimit):
    """
    Operational limit applied to voltage. The use of operational VoltageLimit is preferred instead of limits defined at
      VoltageLevel. The operational VoltageLimits are used, if present.

    normalValue: The normal limit on voltage. High or low limit nature of the limit depends upon the properties of the
      operational limit type. The attribute shall be a positive value or zero.
    value: Limit on voltage. High or low limit nature of the limit depends upon the properties of the operational limit
      type. The attribute shall be a positive value or zero.
    """

    normalValue: float = 0.0  # Type #Voltage in CIM
    value: float = 0.0  # Type #Voltage in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=VoltageLimit"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
