"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ShuntCompensator import ShuntCompensator


@dataclass(config=DataclassConfig)
class LinearShuntCompensator(ShuntCompensator):
    """
    A linear shunt compensator has banks or sections with equal admittance values.

    bPerSection: Positive sequence shunt (charging) susceptance per section.
    gPerSection: Positive sequence shunt (charging) conductance per section.
    b0PerSection: Zero sequence shunt (charging) susceptance per section.
    g0PerSection: Zero sequence shunt (charging) conductance per section.
    """

    bPerSection: float = 0.0  # Type #Susceptance in CIM
    gPerSection: float = 0.0  # Type #Conductance in CIM
    b0PerSection: float = 0.0  # Type #Susceptance in CIM
    g0PerSection: float = 0.0  # Type #Conductance in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=LinearShuntCompensator"]
            + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.SSH.value,
            ],
            # Attributes
            "bPerSection": [
                Profile.EQ.value,
            ],
            "gPerSection": [
                Profile.EQ.value,
            ],
            "b0PerSection": [
                Profile.SC.value,
            ],
            "g0PerSection": [
                Profile.SC.value,
            ],
        }
