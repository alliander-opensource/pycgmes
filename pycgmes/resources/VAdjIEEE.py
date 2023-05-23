"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .VoltageAdjusterDynamics import VoltageAdjusterDynamics


@dataclass
class VAdjIEEE(VoltageAdjusterDynamics):
    """
    IEEE voltage adjuster which is used to represent the voltage adjuster in either a power factor or VAr control
      system. Reference: IEEE 421.5-2005, 11.1.

    vadjf: Set high to provide a continuous raise or lower (VADJF).
    adjslew: Rate at which output of adjuster changes (ADJ_SLEW).  Unit = s / PU.  Typical value = 300.
    vadjmax: Maximum output of the adjuster (VADJMAX) (> VAdjIEEE.vadjmin).  Typical value = 1,1.
    vadjmin: Minimum output of the adjuster (VADJMIN) (< VAdjIEEE.vadjmax).  Typical value = 0,9.
    taon: Time that adjuster pulses are on (TAON) (>= 0).  Typical value = 0,1.
    taoff: Time that adjuster pulses are off (TAOFF) (>= 0).  Typical value = 0,5.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    vadjf: float = 0.0  # Type #Float in CIM
    adjslew: float = 0.0  # Type #Float in CIM
    vadjmax: float = 0.0  # Type #PU in CIM
    vadjmin: float = 0.0  # Type #PU in CIM
    taon: int = 0  # Type #Seconds in CIM
    taoff: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=VAdjIEEE\n"
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
            "vadjf": [
                self.profiles.DY.value,
            ],
            "adjslew": [
                self.profiles.DY.value,
            ],
            "vadjmax": [
                self.profiles.DY.value,
            ],
            "vadjmin": [
                self.profiles.DY.value,
            ],
            "taon": [
                self.profiles.DY.value,
            ],
            "taoff": [
                self.profiles.DY.value,
            ],
        }
