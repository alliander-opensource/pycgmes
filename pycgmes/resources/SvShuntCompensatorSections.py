"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class SvShuntCompensatorSections(Base):
    """
    State variable for the number of sections in service for a shunt compensator.

    ShuntCompensator: The shunt compensator for which the state applies.
    sections: The number of sections in service as a continuous variable. The attribute shall be a positive value or
      zero. To get integer value scale with ShuntCompensator.bPerSection.
    """

    ShuntCompensator: Optional[str] = None  # Type M:1 in CIM
    sections: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=SvShuntCompensatorSections"]
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
                Profile.SV.value,
            ],
            # Attributes
            "ShuntCompensator": [
                Profile.SV.value,
            ],
            "sections": [
                Profile.SV.value,
            ],
        }
