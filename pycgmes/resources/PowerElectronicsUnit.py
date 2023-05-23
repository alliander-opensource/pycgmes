"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .Equipment import Equipment


@dataclass
class PowerElectronicsUnit(Equipment):
    """
    A generating unit or battery or aggregation that connects to the AC network using power electronics rather than
      rotating machines.

    PowerElectronicsConnection: A power electronics unit has a connection to the AC network.
    maxP: Maximum active power limit. This is the maximum (nameplate) limit for the unit.
    minP: Minimum active power limit. This is the minimum (nameplate) limit for the unit.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    # *Association not used*
    # PowerElectronicsConnection : Optional[str] = None  # Type M:1 in CIM
    maxP: float = 0.0  # Type #ActivePower in CIM
    minP: float = 0.0  # Type #ActivePower in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PowerElectronicsUnit\n"
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
                self.profiles.EQ.value,
                self.profiles.SSH.value,
            ],
            # Attributes
            "PowerElectronicsConnection": [
                self.profiles.EQ.value,
            ],
            "maxP": [
                self.profiles.EQ.value,
            ],
            "minP": [
                self.profiles.EQ.value,
            ],
        }
