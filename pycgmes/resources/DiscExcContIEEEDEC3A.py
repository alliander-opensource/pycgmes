"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .DiscontinuousExcitationControlDynamics import (
    DiscontinuousExcitationControlDynamics,
)


@dataclass
class DiscExcContIEEEDEC3A(DiscontinuousExcitationControlDynamics):
    """
    IEEE type DEC3A model. In some systems, the stabilizer output is disconnected from the regulator immediately
      following a severe fault to prevent the stabilizer from competing with action of voltage regulator during the
      first swing. Reference: IEEE 421.5-2005 12.4.

    vtmin: Terminal undervoltage comparison level (VTMIN).
    tdr: Reset time delay (TDR) (>= 0).
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    vtmin: float = 0.0  # Type #PU in CIM
    tdr: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=DiscExcContIEEEDEC3A\n"
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
            "vtmin": [
                self.profiles.DY.value,
            ],
            "tdr": [
                self.profiles.DY.value,
            ],
        }
