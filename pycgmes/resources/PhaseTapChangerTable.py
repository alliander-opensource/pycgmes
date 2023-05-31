"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .IdentifiedObject import IdentifiedObject


@dataclass
class PhaseTapChangerTable(IdentifiedObject):
    """
    Describes a tabular curve for how the phase angle difference and impedance varies with the tap step.

    PhaseTapChangerTablePoint: The points of this table.
    PhaseTapChangerTabular: The phase tap changers to which this phase tap table applies.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # PhaseTapChangerTablePoint : list = field(default_factory=list)  # Type M:1..n in CIM
    # *Association not used*
    # PhaseTapChangerTabular : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PhaseTapChangerTable\n"
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
                self.profiles.EQ.value,
            ],
            # Attributes
            "PhaseTapChangerTablePoint": [
                self.profiles.EQ.value,
            ],
            "PhaseTapChangerTabular": [
                self.profiles.EQ.value,
            ],
        }
