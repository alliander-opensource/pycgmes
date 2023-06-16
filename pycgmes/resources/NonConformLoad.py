"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .EnergyConsumer import EnergyConsumer


@dataclass(config=DataclassConfig)
class NonConformLoad(EnergyConsumer):
    """
    NonConformLoad represents loads that do not follow a daily load change pattern and whose changes are not correlated
      with the daily load change pattern.

    LoadGroup: Group of this ConformLoad.
    """

    LoadGroup: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=NonConformLoad"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.EQ.value,
                Profile.SSH.value,
            ],
            # Attributes
            "LoadGroup": [
                Profile.EQ.value,
            ],
        }
