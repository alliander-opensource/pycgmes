"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .DiscontinuousExcitationControlDynamics import (
    DiscontinuousExcitationControlDynamics,
)


@dataclass
class DiscExcContIEEEDEC2A(DiscontinuousExcitationControlDynamics):
    """
    IEEE type DEC2A model for discontinuous excitation control. This system provides transient excitation boosting via
      an open-loop control as initiated by a trigger signal generated remotely. Reference: IEEE 421.5-2005 12.3.

    vk: Discontinuous controller input reference (VK).
    td1: Discontinuous controller time constant (TD1) (>= 0).
    td2: Discontinuous controller washout time constant (TD2) (>= 0).
    vdmin: Limiter (VDMIN) (< DiscExcContIEEEDEC2A.vdmax).
    vdmax: Limiter (VDMAX) (> DiscExcContIEEEDEC2A.vdmin).
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    vk: float = 0.0  # Type #PU in CIM
    td1: int = 0  # Type #Seconds in CIM
    td2: int = 0  # Type #Seconds in CIM
    vdmin: float = 0.0  # Type #PU in CIM
    vdmax: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=DiscExcContIEEEDEC2A\n"
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
            "vk": [
                self.profiles.DY.value,
            ],
            "td1": [
                self.profiles.DY.value,
            ],
            "td2": [
                self.profiles.DY.value,
            ],
            "vdmin": [
                self.profiles.DY.value,
            ],
            "vdmax": [
                self.profiles.DY.value,
            ],
        }
