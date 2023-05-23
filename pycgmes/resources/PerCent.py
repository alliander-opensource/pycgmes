"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Base import Base


@dataclass
class PerCent(Base):
    """
    Percentage on a defined base.   For example, specify as 100 to indicate at the defined base.

    value: Normally 0 to 100 on a defined base.
    unit:
    multiplier:
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    value: float = 0.0  # Type #Float in CIM
    unit: Optional[str] = None  # Type M:0..1 in CIM
    multiplier: Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PerCent\n"
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
                self.profiles.SC.value,
                self.profiles.SSH.value,
                self.profiles.OP.value,
            ],
            # Attributes
            "value": [
                self.profiles.EQ.value,
                self.profiles.SC.value,
                self.profiles.SSH.value,
                self.profiles.OP.value,
            ],
            "unit": [
                self.profiles.EQ.value,
                self.profiles.SC.value,
                self.profiles.SSH.value,
                self.profiles.OP.value,
            ],
            "multiplier": [
                self.profiles.EQ.value,
                self.profiles.SC.value,
                self.profiles.SSH.value,
                self.profiles.OP.value,
            ],
        }
