"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class SvStatus(Base):
    """
    State variable for status.

    ConductingEquipment: The conducting equipment associated with the status state variable.
    inService: The in service status as a result of topology processing.  It indicates if the equipment is considered as
      energized by the power flow. It reflects if the equipment is connected within a solvable island.
      It does not necessarily reflect whether or not the island was solved by the power flow.
    """

    ConductingEquipment: Optional[str] = None  # Type M:1 in CIM
    inService: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=SvStatus"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.SV.value,
            ],
            # Attributes
            "ConductingEquipment": [
                Profile.SV.value,
            ],
            "inService": [
                Profile.SV.value,
            ],
        }
