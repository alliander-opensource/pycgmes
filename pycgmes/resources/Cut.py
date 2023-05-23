"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Switch import Switch


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ACLineSegment: Optional[str] = None  # Type M:1 in CIM
    lengthFromTerminal1: float = 0.0  # Type #Length in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=Cut\n"
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
            "ACLineSegment": [
                self.profiles.EQ.value,
            ],
            "lengthFromTerminal1": [
                self.profiles.EQ.value,
            ],
        }
