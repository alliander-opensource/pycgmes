"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
class SubGeographicalRegion(IdentifiedObject):
    """
    A subset of a geographical region of a power system network model.

    Region: The geographical region which this sub-geographical region is within.
    Lines: The lines within the sub-geographical region.
    Substations: The substations in this sub-geographical region.
    DCLines: The DC lines in this sub-geographical region.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    Region: Optional[str] = None  # Type M:1..1 in CIM
    # *Association not used*
    # Lines : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # Substations : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # DCLines : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=SubGeographicalRegion\n"
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
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            # Attributes
            "Region": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            "Lines": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            "Substations": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            "DCLines": [
                self.profiles.EQ.value,
            ],
        }
