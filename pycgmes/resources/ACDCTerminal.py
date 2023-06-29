"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
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

    sequenceNumber: int = Field(
        default=0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # OperationalLimitSet : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    BusNameMarker: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    connected: bool = Field(
        default=False,
        in_profiles=[
            Profile.SSH,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # Measurements : list = Field(default_factory=list, in_profiles = [Profile.OP, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.TP,
            Profile.EQBD,
            Profile.EQ,
            Profile.SC,
            Profile.SV,
            Profile.SSH,
            Profile.DY,
            Profile.OP,
        }
