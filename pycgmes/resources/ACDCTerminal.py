"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
class ACDCTerminal(IdentifiedObject):
    """
    An electrical connection point (AC or DC) to a piece of conducting equipment. Terminals are connected at physical
      connection points called connectivity nodes.

    sequenceNumber: The orientation of the terminal connections for a multiple terminal conducting equipment.  The
      sequence numbering starts with 1 and additional terminals should follow in increasing order.
      The first terminal is the `starting point` for a two terminal branch.
    OperationalLimitSet: The operational limit sets at the terminal.
    BusNameMarker: The bus name marker used to name the bus (topological node).
    connected: The connected status is related to a bus-branch model and the topological node to terminal relation.
      True implies the terminal is connected to the related topological node and false implies it is not.
      In a bus-branch model, the connected status is used to tell if equipment is disconnected without
      having to change the connectivity described by the topological node to terminal relation. A valid
      case is that conducting equipment can be connected in one end and open in the other. In particular
      for an AC line segment, where the reactive line charging can be significant, this is a relevant
      case.
    Measurements: Measurements associated with this terminal defining  where the measurement is placed in the network
      topology.  It may be used, for instance, to capture the sensor position, such as a voltage
      transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an
      isolator.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    sequenceNumber: int = 0  # Type #Integer in CIM
    # *Association not used*
    # OperationalLimitSet : list = field(default_factory=list)  # Type M:0..n in CIM
    BusNameMarker: Optional[str] = None  # Type M:0..1 in CIM
    connected: bool = False  # Type #Boolean in CIM
    # *Association not used*
    # Measurements : list = field(default_factory=list)  # Type M:0..n in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ACDCTerminal\n"
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
                self.profiles.SC.value,
                self.profiles.SV.value,
                self.profiles.SSH.value,
                self.profiles.DY.value,
                self.profiles.OP.value,
            ],
            # Attributes
            "sequenceNumber": [
                self.profiles.EQ.value,
            ],
            "OperationalLimitSet": [
                self.profiles.EQ.value,
            ],
            "BusNameMarker": [
                self.profiles.EQ.value,
            ],
            "connected": [
                self.profiles.SSH.value,
            ],
            "Measurements": [
                self.profiles.OP.value,
            ],
        }
