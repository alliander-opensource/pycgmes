"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Base import Base


@dataclass
class VolumeFlowRate(Base):
    """
    Volume per time.

    multiplier:
    unit:
    value:
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    multiplier: Optional[str] = None  # Type M:0..1 in CIM
    unit: Optional[str] = None  # Type M:0..1 in CIM
    value: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=VolumeFlowRate\n"
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
                self.profiles.DY.value,
            ],
            # Attributes
            "multiplier": [
                self.profiles.DY.value,
            ],
            "unit": [
                self.profiles.DY.value,
            ],
            "value": [
                self.profiles.DY.value,
            ],
        }
