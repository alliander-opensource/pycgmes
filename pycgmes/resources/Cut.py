"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Switch import Switch


@dataclass(config=DataclassConfig)
class Cut(Switch):
    """
    A cut separates a line segment into two parts. The cut appears as a switch inserted between these two parts and
      connects them together. As the cut is normally open there is no galvanic connection between the two line
      segment parts. But it is possible to close the cut to get galvanic connection. The cut terminals are oriented
      towards the line segment terminals with the same sequence number. Hence the cut terminal with sequence number
      equal to 1 is oriented to the line segment's terminal with sequence number equal to 1. The cut terminals also
      act as connection points for jumpers and other equipment, e.g. a mobile generator. To enable this,
      connectivity nodes are placed at the cut terminals. Once the connectivity nodes are in place any conducting
      equipment can be connected at them.

    ACLineSegment: The line segment to which the cut is applied.
    lengthFromTerminal1: The length to the place where the cut is located starting from side one of the cut line
      segment, i.e. the line segment Terminal with sequenceNumber equal to 1.
    """

    ACLineSegment: Optional[str] = None  # Type M:1 in CIM
    lengthFromTerminal1: float = 0.0  # Type #Length in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=Cut"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
