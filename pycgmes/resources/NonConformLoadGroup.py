"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .LoadGroup import LoadGroup


@dataclass(config=DataclassConfig)
class NonConformLoadGroup(LoadGroup):
    """
    Loads that do not follow a daily and seasonal load variation pattern.

    EnergyConsumers: Conform loads assigned to this ConformLoadGroup.
    NonConformLoadSchedules: The NonConformLoadSchedules in the NonConformLoadGroup.
    """

    # *Association not used*
    # EnergyConsumers : list = field(default_factory=list)  # Type M:1..n in CIM
    # *Association not used*
    # NonConformLoadSchedules : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=NonConformLoadGroup"]
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
                Profile.EQ.value,
            ],
            # Attributes
            "EnergyConsumers": [
                Profile.EQ.value,
            ],
            "NonConformLoadSchedules": [
                Profile.EQ.value,
            ],
        }
