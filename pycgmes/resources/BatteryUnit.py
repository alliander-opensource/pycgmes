"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PowerElectronicsUnit import PowerElectronicsUnit


@dataclass(config=DataclassConfig)
class BatteryUnit(PowerElectronicsUnit):
    """
    An electrochemical energy storage device.

    ratedE: Full energy storage capacity of the battery. The attribute shall be a positive value.
    batteryState: The current state of the battery (charging, full, etc.).
    storedE: Amount of energy currently stored. The attribute shall be a positive value or zero and lower than
      BatteryUnit.ratedE.
    """

    ratedE: float = 0.0  # Type #RealEnergy in CIM
    batteryState: Optional[str] = None  # Type M:1..1 in CIM
    storedE: float = 0.0  # Type #RealEnergy in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=BatteryUnit"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "ratedE": [
                Profile.EQ.value,
            ],
            "batteryState": [
                Profile.SSH.value,
            ],
            "storedE": [
                Profile.SSH.value,
            ],
        }
