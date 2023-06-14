"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
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

        return "\n".join(
            ["class=MutualCoupling"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.SC.value,
            ],
            # Attributes
            "b0ch": [
                Profile.SC.value,
            ],
            "distance11": [
                Profile.SC.value,
            ],
            "distance12": [
                Profile.SC.value,
            ],
            "distance21": [
                Profile.SC.value,
            ],
            "distance22": [
                Profile.SC.value,
            ],
            "g0ch": [
                Profile.SC.value,
            ],
            "r0": [
                Profile.SC.value,
            ],
            "x0": [
                Profile.SC.value,
            ],
            "Second_Terminal": [
                Profile.SC.value,
            ],
            "First_Terminal": [
                Profile.SC.value,
            ],
        }
