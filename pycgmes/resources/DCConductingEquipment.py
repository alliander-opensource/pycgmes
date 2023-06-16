"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Equipment import Equipment


@dataclass(config=DataclassConfig)
class DCConductingEquipment(Equipment):
    """
    The parts of the DC power system that are designed to carry current or that are conductively connected through DC
      terminals.

    ratedUdc: Rated DC device voltage. The attribute shall be a positive value. It is configuration data used in power
      flow.
    DCTerminals: A DC conducting equipment has DC terminals.
    """

    ratedUdc: float = 0.0  # Type #Voltage in CIM
    # *Association not used*
    # DCTerminals : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=DCConductingEquipment"]
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
            "ratedUdc": [
                Profile.EQ.value,
            ],
            "DCTerminals": [
                Profile.EQ.value,
            ],
        }
