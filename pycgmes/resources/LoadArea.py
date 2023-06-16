"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .EnergyArea import EnergyArea


@dataclass(config=DataclassConfig)
class LoadArea(EnergyArea):
    """
    The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow
      load scaling.

    SubLoadAreas: The SubLoadAreas in the LoadArea.
    """

    # *Association not used*
    # SubLoadAreas : list = field(default_factory=list)  # Type M:1..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=LoadArea"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "SubLoadAreas": [
                Profile.EQ.value,
            ],
        }
