"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class OperationalLimit(IdentifiedObject):
    """
    A value and normal value associated with a specific kind of limit.  The sub class value and normalValue attributes
      vary inversely to the associated OperationalLimitType.acceptableDuration (acceptableDuration for short).   If
      a particular piece of equipment has multiple operational limits of the same kind (apparent power, current,
      etc.), the limit with the greatest acceptableDuration shall have the smallest limit value and the limit with
      the smallest acceptableDuration shall have the largest limit value.  Note: A large current can only be allowed
      to flow through a piece of equipment for a short duration without causing damage, but a lesser current can be
      allowed to flow for a longer duration.

    OperationalLimitSet: The limit set to which the limit values belong.
    OperationalLimitType: The limit type associated with this limit.
    """

    OperationalLimitSet: Optional[str] = None  # Type M:1 in CIM
    OperationalLimitType: Optional[str] = None  # Type M:1..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=OperationalLimit"]
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
            "OperationalLimitSet": [
                Profile.EQ.value,
            ],
            "OperationalLimitType": [
                Profile.EQ.value,
            ],
        }
