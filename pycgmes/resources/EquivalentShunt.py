"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .EquivalentEquipment import EquivalentEquipment


@dataclass(config=DataclassConfig)
class EquivalentShunt(EquivalentEquipment):
    """
    The class represents equivalent shunts.

    b: Positive sequence shunt susceptance.
    g: Positive sequence shunt conductance.
    """

    b: float = 0.0  # Type #Susceptance in CIM
    g: float = 0.0  # Type #Conductance in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=EquivalentShunt"]
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
            "b": [
                Profile.EQ.value,
            ],
            "g": [
                Profile.EQ.value,
            ],
        }
