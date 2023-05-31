"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .Conductor import Conductor


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=ACLineSegment\n"
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
                self.profiles.SC.value,
            ],
            # Attributes
            "bch": [
                self.profiles.EQ.value,
            ],
            "gch": [
                self.profiles.EQ.value,
            ],
            "r": [
                self.profiles.EQ.value,
            ],
            "x": [
                self.profiles.EQ.value,
            ],
            "Clamp": [
                self.profiles.EQ.value,
            ],
            "Cut": [
                self.profiles.EQ.value,
            ],
            "b0ch": [
                self.profiles.SC.value,
            ],
            "g0ch": [
                self.profiles.SC.value,
            ],
            "r0": [
                self.profiles.SC.value,
            ],
            "shortCircuitEndTemperature": [
                self.profiles.SC.value,
            ],
            "x0": [
                self.profiles.SC.value,
            ],
        }
