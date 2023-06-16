"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ConnectivityNodeContainer import ConnectivityNodeContainer


@dataclass(config=DataclassConfig)
class EquipmentContainer(ConnectivityNodeContainer):
    """
    A modelling construct to provide a root class for containing equipment.

    Equipments: Contained equipment.
    """

    # *Association not used*
    # Equipments : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=EquipmentContainer"]
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
            "Equipments": [
                Profile.EQBD.value,
                Profile.EQ.value,
            ],
        }
