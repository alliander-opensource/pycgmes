"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Equipment import Equipment


@dataclass(config=DataclassConfig)
class ConductingEquipment(Equipment):
    """
    The parts of the AC power system that are designed to carry current or that are conductively connected through
      terminals.

    Terminals: Conducting equipment have terminals that may be connected to other conducting equipment terminals via
      connectivity nodes or topological nodes.
    BaseVoltage: Base voltage of this conducting equipment.  Use only when there is no voltage level container used and
      only one base voltage applies.  For example, not used for transformers.
    SvStatus: The status state variable associated with this conducting equipment.
    """

    # *Association not used*
    # Terminals : list = field(default_factory=list)  # Type M:0..n in CIM
    BaseVoltage: Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # SvStatus : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ConductingEquipment"]
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
                Profile.SC.value,
                Profile.SV.value,
                Profile.SSH.value,
                Profile.DY.value,
            ],
            # Attributes
            "Terminals": [
                Profile.EQBD.value,
                Profile.EQ.value,
                Profile.DY.value,
            ],
            "BaseVoltage": [
                Profile.EQ.value,
            ],
            "SvStatus": [
                Profile.SV.value,
            ],
        }
