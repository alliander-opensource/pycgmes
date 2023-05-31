"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Base import Base


@dataclass
class SvTapStep(Base):
    """
    State variable for transformer tap step.

    position: The floating point tap position.   This is not the tap ratio, but rather the tap step position as defined
      by the related tap changer model and normally is constrained to be within the range of minimum and
      maximum tap positions.
    TapChanger: The tap changer associated with the tap step state.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    position: float = 0.0  # Type #Float in CIM
    TapChanger: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=SvTapStep\n"
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
                self.profiles.SV.value,
            ],
            # Attributes
            "position": [
                self.profiles.SV.value,
            ],
            "TapChanger": [
                self.profiles.SV.value,
            ],
        }
