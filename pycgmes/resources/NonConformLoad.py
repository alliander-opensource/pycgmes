"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .EnergyConsumer import EnergyConsumer


@dataclass
class NonConformLoad(EnergyConsumer):
    """
    NonConformLoad represents loads that do not follow a daily load change pattern and whose changes are not correlated
      with the daily load change pattern.

    LoadGroup: Group of this ConformLoad.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    LoadGroup: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=NonConformLoad\n"
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
                self.profiles.SSH.value,
            ],
            # Attributes
            "LoadGroup": [
                self.profiles.EQ.value,
            ],
        }
