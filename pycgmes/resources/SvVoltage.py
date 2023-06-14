"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Base import Base


@dataclass(config=DataclassConfig)
class SvVoltage(Base):
    """
    State variable for voltage.

    angle: The voltage angle of the topological node complex voltage with respect to system reference.
    v: The voltage magnitude at the topological node. The attribute shall be a positive value.
    TopologicalNode: The topological node associated with the voltage state.
    """

    angle: float = 0.0  # Type #AngleDegrees in CIM
    v: float = 0.0  # Type #Voltage in CIM
    TopologicalNode: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=SvVoltage"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.SV.value,
            ],
            # Attributes
            "angle": [
                Profile.SV.value,
            ],
            "v": [
                Profile.SV.value,
            ],
            "TopologicalNode": [
                Profile.SV.value,
            ],
        }
