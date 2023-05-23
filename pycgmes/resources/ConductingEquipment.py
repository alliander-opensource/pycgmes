"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Equipment import Equipment


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # Terminals : list = field(default_factory=list)  # Type M:0..n in CIM
    BaseVoltage: Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # SvStatus : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ConductingEquipment\n"
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
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
                self.profiles.SC.value,
                self.profiles.SV.value,
                self.profiles.SSH.value,
                self.profiles.DY.value,
            ],
            # Attributes
            "Terminals": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
                self.profiles.DY.value,
            ],
            "BaseVoltage": [
                self.profiles.EQ.value,
            ],
            "SvStatus": [
                self.profiles.SV.value,
            ],
        }
