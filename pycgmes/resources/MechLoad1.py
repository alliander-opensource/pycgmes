"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .MechanicalLoadDynamics import MechanicalLoadDynamics


@dataclass
class MechLoad1(MechanicalLoadDynamics):
    """
    Mechanical load model type 1.

    a: Speed squared coefficient (a).
    b: Speed coefficient (b).
    d: Speed to the exponent coefficient (d).
    e: Exponent (e).
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    a: float = 0.0  # Type #Float in CIM
    b: float = 0.0  # Type #Float in CIM
    d: float = 0.0  # Type #Float in CIM
    e: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=MechLoad1\n"
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
                self.profiles.DY.value,
            ],
            # Attributes
            "a": [
                self.profiles.DY.value,
            ],
            "b": [
                self.profiles.DY.value,
            ],
            "d": [
                self.profiles.DY.value,
            ],
            "e": [
                self.profiles.DY.value,
            ],
        }
