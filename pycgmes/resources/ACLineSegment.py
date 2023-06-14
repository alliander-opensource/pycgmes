"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
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

    bch: float = 0.0  # Type #Susceptance in CIM
    gch: float = 0.0  # Type #Conductance in CIM
    r: float = 0.0  # Type #Resistance in CIM
    x: float = 0.0  # Type #Reactance in CIM
    # *Association not used*
    # Clamp : list = field(default_factory=list)  # Type M:0..n in CIM
    # *Association not used*
    # Cut : list = field(default_factory=list)  # Type M:0..n in CIM
    b0ch: float = 0.0  # Type #Susceptance in CIM
    g0ch: float = 0.0  # Type #Conductance in CIM
    r0: float = 0.0  # Type #Resistance in CIM
    shortCircuitEndTemperature: float = 0.0  # Type #Temperature in CIM
    x0: float = 0.0  # Type #Reactance in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ACLineSegment"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.SC.value,
            ],
            # Attributes
            "bch": [
                Profile.EQ.value,
            ],
            "gch": [
                Profile.EQ.value,
            ],
            "r": [
                Profile.EQ.value,
            ],
            "x": [
                Profile.EQ.value,
            ],
            "Clamp": [
                Profile.EQ.value,
            ],
            "Cut": [
                Profile.EQ.value,
            ],
            "b0ch": [
                Profile.SC.value,
            ],
            "g0ch": [
                Profile.SC.value,
            ],
            "r0": [
                Profile.SC.value,
            ],
            "shortCircuitEndTemperature": [
                Profile.SC.value,
            ],
            "x0": [
                Profile.SC.value,
            ],
        }
