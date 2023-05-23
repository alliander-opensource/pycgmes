"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Base import Base


@dataclass
class SvShuntCompensatorSections(Base):
    """
    State variable for the number of sections in service for a shunt compensator.

    ShuntCompensator: The shunt compensator for which the state applies.
    sections: The number of sections in service as a continuous variable. The attribute shall be a positive value or
      zero. To get integer value scale with ShuntCompensator.bPerSection.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ShuntCompensator: Optional[str] = None  # Type M:1 in CIM
    sections: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=SvShuntCompensatorSections\n"
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
            "ShuntCompensator": [
                self.profiles.SV.value,
            ],
            "sections": [
                self.profiles.SV.value,
            ],
        }
