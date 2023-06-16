"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ConductingEquipment import ConductingEquipment


@dataclass(config=DataclassConfig)
class Clamp(ConductingEquipment):
    """
    A Clamp is a galvanic connection at a line segment where other equipment is connected. A Clamp does not cut the line
      segment.  A Clamp is ConductingEquipment and has one Terminal with an associated ConnectivityNode. Any other
      ConductingEquipment can be connected to the Clamp ConnectivityNode.

    ACLineSegment: The line segment to which the clamp is connected.
    lengthFromTerminal1: The length to the place where the clamp is located starting from side one of the line segment,
      i.e. the line segment terminal with sequence number equal to 1.
    """

    ACLineSegment: Optional[str] = None  # Type M:1 in CIM
    lengthFromTerminal1: float = 0.0  # Type #Length in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=Clamp"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "ACLineSegment": [
                Profile.EQ.value,
            ],
            "lengthFromTerminal1": [
                Profile.EQ.value,
            ],
        }
