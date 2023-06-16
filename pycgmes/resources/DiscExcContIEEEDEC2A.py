"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics


@dataclass(config=DataclassConfig)
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

    vk: float = 0.0  # Type #PU in CIM
    td1: int = 0  # Type #Seconds in CIM
    td2: int = 0  # Type #Seconds in CIM
    vdmin: float = 0.0  # Type #PU in CIM
    vdmax: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=DiscExcContIEEEDEC2A"]
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
                Profile.DY.value,
            ],
            # Attributes
            "vk": [
                Profile.DY.value,
            ],
            "td1": [
                Profile.DY.value,
            ],
            "td2": [
                Profile.DY.value,
            ],
            "vdmin": [
                Profile.DY.value,
            ],
            "vdmax": [
                Profile.DY.value,
            ],
        }
