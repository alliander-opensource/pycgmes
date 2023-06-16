"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .Equipment import Equipment


@dataclass(config=DataclassConfig)
class PowerElectronicsUnit(Equipment):
    """
    A generating unit or battery or aggregation that connects to the AC network using power electronics rather than
      rotating machines.

    PowerElectronicsConnection: A power electronics unit has a connection to the AC network.
    maxP: Maximum active power limit. This is the maximum (nameplate) limit for the unit.
    minP: Minimum active power limit. This is the minimum (nameplate) limit for the unit.
    """

    # *Association not used*
    # PowerElectronicsConnection : Optional[str] = None  # Type M:1 in CIM
    maxP: float = 0.0  # Type #ActivePower in CIM
    minP: float = 0.0  # Type #ActivePower in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PowerElectronicsUnit"]
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
                Profile.EQ.value,
                Profile.SSH.value,
            ],
            # Attributes
            "PowerElectronicsConnection": [
                Profile.EQ.value,
            ],
            "maxP": [
                Profile.EQ.value,
            ],
            "minP": [
                Profile.EQ.value,
            ],
        }
