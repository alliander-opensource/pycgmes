"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .IdentifiedObject import IdentifiedObject


@dataclass
class MutualCoupling(IdentifiedObject):
    """
    This class represents the zero sequence line mutual coupling.

    b0ch: Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section.
    distance11: Distance to the start of the coupled region from the first line`s terminal having sequence number equal
      to 1.
    distance12: Distance to the end of the coupled region from the first line`s terminal with sequence number equal to
      1.
    distance21: Distance to the start of coupled region from the second line`s terminal with sequence number equal to 1.
    distance22: Distance to the end of coupled region from the second line`s terminal with sequence number equal to 1.
    g0ch: Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section.
    r0: Zero sequence branch-to-branch mutual impedance coupling, resistance.
    x0: Zero sequence branch-to-branch mutual impedance coupling, reactance.
    Second_Terminal: The starting terminal for the calculation of distances along the second branch of the mutual
      coupling.
    First_Terminal: The starting terminal for the calculation of distances along the first branch of the mutual
      coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The
      first and second terminals of a mutual coupling should point to different AC line segments.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    b0ch: float = 0.0  # Type #Susceptance in CIM
    distance11: float = 0.0  # Type #Length in CIM
    distance12: float = 0.0  # Type #Length in CIM
    distance21: float = 0.0  # Type #Length in CIM
    distance22: float = 0.0  # Type #Length in CIM
    g0ch: float = 0.0  # Type #Conductance in CIM
    r0: float = 0.0  # Type #Resistance in CIM
    x0: float = 0.0  # Type #Reactance in CIM
    Second_Terminal: Optional[str] = None  # Type M:1 in CIM
    First_Terminal: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=MutualCoupling\n"
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
                self.profiles.SC.value,
            ],
            # Attributes
            "b0ch": [
                self.profiles.SC.value,
            ],
            "distance11": [
                self.profiles.SC.value,
            ],
            "distance12": [
                self.profiles.SC.value,
            ],
            "distance21": [
                self.profiles.SC.value,
            ],
            "distance22": [
                self.profiles.SC.value,
            ],
            "g0ch": [
                self.profiles.SC.value,
            ],
            "r0": [
                self.profiles.SC.value,
            ],
            "x0": [
                self.profiles.SC.value,
            ],
            "Second_Terminal": [
                self.profiles.SC.value,
            ],
            "First_Terminal": [
                self.profiles.SC.value,
            ],
        }
