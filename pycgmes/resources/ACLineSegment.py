"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Conductor import Conductor


@dataclass(config=DataclassConfig)
class ACLineSegment(Conductor):
    """
    A wire or combination of wires, with consistent electrical characteristics, building a single electrical system,
      used to carry alternating current between points in the power system. For symmetrical, transposed three phase
      lines, it is sufficient to use attributes of the line segment, which describe impedances and admittances for
      the entire length of the segment.  Additionally impedances can be computed by using length and associated per
      length impedances. The BaseVoltage at the two ends of ACLineSegments in a Line shall have the same
      BaseVoltage.nominalVoltage. However, boundary lines may have slightly different BaseVoltage.nominalVoltages
      and variation is allowed. Larger voltage difference in general requires use of an equivalent branch.

    bch: Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value
      represents the full charging over the full length of the line.
    gch: Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
    r: Positive sequence series resistance of the entire line section.
    x: Positive sequence series reactance of the entire line section.
    Clamp: The clamps connected to the line segment.
    Cut: Cuts applied to the line segment.
    b0ch: Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
    g0ch: Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
    r0: Zero sequence series resistance of the entire line section.
    shortCircuitEndTemperature: Maximum permitted temperature at the end of SC for the calculation of minimum short-
      circuit currents. Used for short circuit data exchange according to IEC 60909.
    x0: Zero sequence series reactance of the entire line section.
    """

    bch: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    gch: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    r: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    x: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # Clamp : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # Cut : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    b0ch: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    g0ch: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    r0: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    shortCircuitEndTemperature: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    x0: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SC,
        }
