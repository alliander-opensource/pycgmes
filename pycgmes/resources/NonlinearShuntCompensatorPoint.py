"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Base import Base


@dataclass
class NonlinearShuntCompensatorPoint(Base):
    """
    A non linear shunt compensator bank or section admittance value. The number of NonlinearShuntCompenstorPoint
      instances associated with a NonlinearShuntCompensator shall be equal to ShuntCompensator.maximumSections.
      ShuntCompensator.sections shall only be set to one of the NonlinearShuntCompenstorPoint.sectionNumber. There
      is no interpolation between NonlinearShuntCompenstorPoint-s.

    NonlinearShuntCompensator: Non-linear shunt compensator owning this point.
    b: Positive sequence shunt (charging) susceptance per section.
    g: Positive sequence shunt (charging) conductance per section.
    sectionNumber: The number of the section.
    b0: Zero sequence shunt (charging) susceptance per section.
    g0: Zero sequence shunt (charging) conductance per section.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    NonlinearShuntCompensator: Optional[str] = None  # Type M:1 in CIM
    b: float = 0.0  # Type #Susceptance in CIM
    g: float = 0.0  # Type #Conductance in CIM
    sectionNumber: int = 0  # Type #Integer in CIM
    b0: float = 0.0  # Type #Susceptance in CIM
    g0: float = 0.0  # Type #Conductance in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=NonlinearShuntCompensatorPoint\n"
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
            "NonlinearShuntCompensator": [
                self.profiles.EQ.value,
            ],
            "b": [
                self.profiles.EQ.value,
            ],
            "g": [
                self.profiles.EQ.value,
            ],
            "sectionNumber": [
                self.profiles.EQ.value,
            ],
            "b0": [
                self.profiles.SC.value,
            ],
            "g0": [
                self.profiles.SC.value,
            ],
        }
