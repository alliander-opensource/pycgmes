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
class OperationalLimitType(IdentifiedObject):
    """
    The operational meaning of a category of limits.

    OperationalLimit: The operational limits associated with this type of limit.
    acceptableDuration: The nominal acceptable duration of the limit. Limits are commonly expressed in terms of the time
      limit for which the limit is normally acceptable. The actual acceptable duration of a
      specific limit may depend on other local factors such as temperature or wind speed. The
      attribute has meaning only if the flag isInfiniteDuration is set to false, hence it shall
      not be exchanged when isInfiniteDuration is set to true.
    direction: The direction of the limit.
    isInfiniteDuration: Defines if the operational limit type has infinite duration. If true, the limit has infinite
      duration. If false, the limit has definite duration which is defined by the attribute
      acceptableDuration.
    kind: Types of limits defined in the ENTSO-E Operational Handbook Policy 3.
    """

    # *Association not used*
    # OperationalLimit : list = field(default_factory=list)  # Type M:0..n in CIM
    acceptableDuration: int = 0  # Type #Seconds in CIM
    direction: Optional[str] = None  # Type M:1..1 in CIM
    isInfiniteDuration: bool = False  # Type #Boolean in CIM
    kind: Optional[str] = None  # Type M:1..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=OperationalLimitType"]
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
            ],
            # Attributes
            "OperationalLimit": [
                Profile.EQ.value,
            ],
            "acceptableDuration": [
                Profile.EQ.value,
            ],
            "direction": [
                Profile.EQ.value,
            ],
            "isInfiniteDuration": [
                Profile.EQ.value,
            ],
            "kind": [
                Profile.EQ.value,
            ],
        }
