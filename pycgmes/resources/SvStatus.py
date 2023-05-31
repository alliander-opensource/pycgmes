"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Base import Base


@dataclass
class SvStatus(Base):
    """
    State variable for status.

    ConductingEquipment: The conducting equipment associated with the status state variable.
    inService: The in service status as a result of topology processing.  It indicates if the equipment is considered as
      energized by the power flow. It reflects if the equipment is connected within a solvable island.
      It does not necessarily reflect whether or not the island was solved by the power flow.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ConductingEquipment: Optional[str] = None  # Type M:1 in CIM
    inService: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=SvStatus\n"
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
                self.profiles.SV.value,
            ],
            # Attributes
            "ConductingEquipment": [
                self.profiles.SV.value,
            ],
            "inService": [
                self.profiles.SV.value,
            ],
        }
