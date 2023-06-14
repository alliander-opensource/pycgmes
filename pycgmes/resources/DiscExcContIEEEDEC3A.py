"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics


@dataclass(config=DataclassConfig)
class DiscExcContIEEEDEC3A(DiscontinuousExcitationControlDynamics):
    """
    IEEE type DEC3A model. In some systems, the stabilizer output is disconnected from the regulator immediately
      following a severe fault to prevent the stabilizer from competing with action of voltage regulator during the
      first swing. Reference: IEEE 421.5-2005 12.4.

    vtmin: Terminal undervoltage comparison level (VTMIN).
    tdr: Reset time delay (TDR) (>= 0).
    """

    vtmin: float = 0.0  # Type #PU in CIM
    tdr: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=DiscExcContIEEEDEC3A"]
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
            "vtmin": [
                Profile.DY.value,
            ],
            "tdr": [
                Profile.DY.value,
            ],
        }
