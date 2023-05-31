"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .TapChangerTablePoint import TapChangerTablePoint


@dataclass
class RatioTapChangerTablePoint(TapChangerTablePoint):
    """
    Describes each tap step in the ratio tap changer tabular curve.

    RatioTapChangerTable: Table of this point.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    RatioTapChangerTable: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=RatioTapChangerTablePoint\n"
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
            "RatioTapChangerTable": [
                self.profiles.EQ.value,
            ],
        }
