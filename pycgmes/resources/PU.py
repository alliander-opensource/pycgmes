"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Base import Base


@dataclass
class PU(Base):
    """
    Per Unit - a positive or negative value referred to a defined base. Values typically range from -10 to +10.

    value:
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
        str_ = "class=PU\n"
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
                self.profiles.SC.value,
                self.profiles.SSH.value,
                self.profiles.DY.value,
            ],
            # Attributes
            "value": [
                self.profiles.SC.value,
                self.profiles.SSH.value,
                self.profiles.DY.value,
            ],
            "unit": [
                self.profiles.SC.value,
                self.profiles.SSH.value,
                self.profiles.DY.value,
            ],
            "multiplier": [
                self.profiles.SC.value,
                self.profiles.SSH.value,
                self.profiles.DY.value,
            ],
        }
