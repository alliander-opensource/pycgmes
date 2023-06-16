"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ConnectivityNodeContainer import ConnectivityNodeContainer


@dataclass(config=DataclassConfig)
class EquivalentNetwork(ConnectivityNodeContainer):
    """
    A class that groups electrical equivalents, including internal nodes, of a network that has been reduced. The
      ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The
      boundary Connectivity nodes where the equivalent connects outside itself are not contained by the equivalent.

    EquivalentEquipments: The associated reduced equivalents.
    """

    # *Association not used*
    # EquivalentEquipments : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=EquivalentNetwork"]
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
            "EquivalentEquipments": [
                Profile.EQ.value,
            ],
        }
