"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ShuntCompensator import ShuntCompensator


@dataclass
class LinearShuntCompensator(ShuntCompensator):
    """
    A linear shunt compensator has banks or sections with equal admittance values.

    bPerSection: Positive sequence shunt (charging) susceptance per section.
    gPerSection: Positive sequence shunt (charging) conductance per section.
    b0PerSection: Zero sequence shunt (charging) susceptance per section.
    g0PerSection: Zero sequence shunt (charging) conductance per section.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    bPerSection: float = 0.0  # Type #Susceptance in CIM
    gPerSection: float = 0.0  # Type #Conductance in CIM
    b0PerSection: float = 0.0  # Type #Susceptance in CIM
    g0PerSection: float = 0.0  # Type #Conductance in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=LinearShuntCompensator\n"
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
                self.profiles.SSH.value,
            ],
            # Attributes
            "bPerSection": [
                self.profiles.EQ.value,
            ],
            "gPerSection": [
                self.profiles.EQ.value,
            ],
            "b0PerSection": [
                self.profiles.SC.value,
            ],
            "g0PerSection": [
                self.profiles.SC.value,
            ],
        }
