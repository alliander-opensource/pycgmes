"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .EnergyConsumer import EnergyConsumer


@dataclass
class ConformLoad(EnergyConsumer):
    """
    ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load
      with a system load.

    LoadGroup: Group of this ConformLoad.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    LoadGroup: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ConformLoad\n"
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
