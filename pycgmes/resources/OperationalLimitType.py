"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # OperationalLimit : list = field(default_factory=list)  # Type M:0..n in CIM
    acceptableDuration: int = 0  # Type #Seconds in CIM
    direction: Optional[str] = None  # Type M:1..1 in CIM
    isInfiniteDuration: bool = False  # Type #Boolean in CIM
    kind: Optional[str] = None  # Type M:1..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=OperationalLimitType\n"
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
            ],
            # Attributes
            "OperationalLimit": [
                self.profiles.EQ.value,
            ],
            "acceptableDuration": [
                self.profiles.EQ.value,
            ],
            "direction": [
                self.profiles.EQ.value,
            ],
            "isInfiniteDuration": [
                self.profiles.EQ.value,
            ],
            "kind": [
                self.profiles.EQ.value,
            ],
        }
