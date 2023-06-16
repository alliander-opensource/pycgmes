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
class OperationalLimitSet(IdentifiedObject):
    """
    A set of limits associated with equipment.  Sets of limits might apply to a specific temperature, or season for
      example. A set of limits may contain different severities of limit levels that would apply to the same
      equipment. The set may contain limits of different types such as apparent power and current limits or high and
      low voltage limits  that are logically applied together as a set.

    Terminal: The terminal where the operational limit set apply.
    Equipment: The equipment to which the limit set applies.
    OperationalLimitValue: Values of equipment limits.
    """

    Terminal: Optional[str] = None  # Type M:1 in CIM
    Equipment: Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # OperationalLimitValue : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=OperationalLimitSet"]
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
            "Terminal": [
                Profile.EQ.value,
            ],
            "Equipment": [
                Profile.EQ.value,
            ],
            "OperationalLimitValue": [
                Profile.EQ.value,
            ],
        }
