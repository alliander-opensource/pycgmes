"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
class BaseVoltage(IdentifiedObject):
    """
    Defines a system base voltage which is referenced.

    TopologicalNode: The topological nodes at the base voltage.
    nominalVoltage: The power system resource`s base voltage.  Shall be a positive value and not zero.
    VoltageLevel: The voltage levels having this base voltage.
    ConductingEquipment: All conducting equipment with this base voltage.  Use only when there is no voltage level
      container used and only one base voltage applies.  For example, not used for
      transformers.
    TransformerEnds: Transformer ends at the base voltage.  This is essential for PU calculation.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # TopologicalNode : list = field(default_factory=list)  # Type M:0..n in CIM
    nominalVoltage: float = 0.0  # Type #Voltage in CIM
    # *Association not used*
    # VoltageLevel : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # ConductingEquipment : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # TransformerEnds : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=BaseVoltage\n"
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
                self.profiles.TP.value,
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            # Attributes
            "TopologicalNode": [
                self.profiles.TP.value,
            ],
            "nominalVoltage": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            "VoltageLevel": [
                self.profiles.EQBD.value,
                self.profiles.EQ.value,
            ],
            "ConductingEquipment": [
                self.profiles.EQ.value,
            ],
            "TransformerEnds": [
                self.profiles.EQ.value,
            ],
        }
