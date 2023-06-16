"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .MechanicalLoadDynamics import MechanicalLoadDynamics


@dataclass(config=DataclassConfig)
class MechLoad1(MechanicalLoadDynamics):
    """
    Mechanical load model type 1.

    a: Speed squared coefficient (a).
    b: Speed coefficient (b).
    d: Speed to the exponent coefficient (d).
    e: Exponent (e).
    """

    a: float = 0.0  # Type #Float in CIM
    b: float = 0.0  # Type #Float in CIM
    d: float = 0.0  # Type #Float in CIM
    e: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=MechLoad1"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.DY.value,
            ],
            # Attributes
            "a": [
                Profile.DY.value,
            ],
            "b": [
                Profile.DY.value,
            ],
            "d": [
                Profile.DY.value,
            ],
            "e": [
                Profile.DY.value,
            ],
        }
