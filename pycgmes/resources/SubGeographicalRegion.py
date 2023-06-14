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
class SubGeographicalRegion(IdentifiedObject):
    """
    A subset of a geographical region of a power system network model.

    Region: The geographical region which this sub-geographical region is within.
    Lines: The lines within the sub-geographical region.
    Substations: The substations in this sub-geographical region.
    DCLines: The DC lines in this sub-geographical region.
    """

    Region: Optional[str] = None  # Type M:1..1 in CIM
    # *Association not used*
    # Lines : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # Substations : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # DCLines : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=SubGeographicalRegion"]
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
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
            # Attributes
            "Region": [
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
            "Lines": [
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
            "Substations": [
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
            "DCLines": [
                Profile.EQ.value,
            ],
        }
