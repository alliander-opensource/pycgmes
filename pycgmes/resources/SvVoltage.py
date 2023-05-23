"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .Base import Base


@dataclass
class SvVoltage(Base):
    """
    State variable for voltage.

    angle: The voltage angle of the topological node complex voltage with respect to system reference.
    v: The voltage magnitude at the topological node. The attribute shall be a positive value.
    TopologicalNode: The topological node associated with the voltage state.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    angle: float = 0.0  # Type #AngleDegrees in CIM
    v: float = 0.0  # Type #Voltage in CIM
    TopologicalNode: Optional[str] = None  # Type M:1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=SvVoltage\n"
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
                self.profiles.SV.value,
            ],
            # Attributes
            "angle": [
                self.profiles.SV.value,
            ],
            "v": [
                self.profiles.SV.value,
            ],
            "TopologicalNode": [
                self.profiles.SV.value,
            ],
        }
