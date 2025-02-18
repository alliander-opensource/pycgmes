"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass
class ACDCTerminal(IdentifiedObject):
    """
    An electrical connection point (AC or DC) to a piece of conducting equipment. Terminals are connected at physical
      connection points called connectivity nodes.

    BusNameMarker: The bus name marker used to name the bus (topological node).
    Measurements: Measurements associated with this terminal defining  where the measurement is placed in the network
      topology.  It may be used, for instance, to capture the sensor position, such as a voltage
      transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an
      isolator.
    OperationalLimitSet: The operational limit sets at the terminal.
    connected: The connected status is related to a bus-branch model and the topological node to terminal relation.
      True implies the terminal is connected to the related topological node and false implies it is not.
      In a bus-branch model, the connected status is used to tell if equipment is disconnected without
      having to change the connectivity described by the topological node to terminal relation. A valid
      case is that conducting equipment can be connected in one end and open in the other. In particular
      for an AC line segment, where the reactive line charging can be significant, this is a relevant
      case.
    sequenceNumber: The orientation of the terminal connections for a multiple terminal conducting equipment.  The
      sequence numbering starts with 1 and additional terminals should follow in increasing order.
      The first terminal is the `starting point` for a two terminal branch.
    """

    BusNameMarker: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": True,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": False,
        },
    )

    Measurements: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.OP,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    OperationalLimitSet: list = Field(
        default_factory=list,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": False,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": True,
            "is_primitive_attribute": False,
        },
    )

    connected: bool = Field(
        default=False,
        json_schema_extra={
            "in_profiles": [
                Profile.SSH,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    sequenceNumber: int = Field(
        default=0,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ],
            "is_used": True,
            "is_class_attribute": False,
            "is_enum_attribute": False,
            "is_list_attribute": False,
            "is_primitive_attribute": True,
        },
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
            Profile.EQ,
            Profile.EQBD,
            Profile.OP,
            Profile.SC,
            Profile.SSH,
            Profile.SV,
            Profile.TP,
        }

    @cached_property
    def recommended_profile(self) -> BaseProfile:
        """
        This is the profile with most of the attributes.
        It should be used to write the data to as few as possible files.
        """
        return Profile.EQ
