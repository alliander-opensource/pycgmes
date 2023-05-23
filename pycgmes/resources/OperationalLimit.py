"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    OperationalLimitSet: Optional[str] = None  # Type M:1 in CIM
    OperationalLimitType: Optional[str] = None  # Type M:1..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=OperationalLimit\n"
        attributes = self.__dict__
        for key, val in attributes.items():
            str_ = str_ + key + f"={val}\n"
        return str_

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                self.profiles.EQ.value,
                self.profiles.SSH.value,
            ],
            # Attributes
            "OperationalLimitSet": [
                self.profiles.EQ.value,
            ],
            "OperationalLimitType": [
                self.profiles.EQ.value,
            ],
        }
