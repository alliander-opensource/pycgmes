"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .PhaseTapChanger import PhaseTapChanger


@dataclass
class PhaseTapChangerTabular(PhaseTapChanger):
    """
    Describes a tap changer with a table defining the relation between the tap step and the phase angle difference
      across the transformer.

    PhaseTapChangerTable: The phase tap changer table for this phase tap changer.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    PhaseTapChangerTable: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PhaseTapChangerTabular\n"
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
                self.profiles.SSH.value,
            ],
            # Attributes
            "PhaseTapChangerTable": [
                self.profiles.EQ.value,
            ],
        }
