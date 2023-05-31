"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .PowerElectronicsUnit import PowerElectronicsUnit


@dataclass
class BatteryUnit(PowerElectronicsUnit):
    """
    An electrochemical energy storage device.

    ratedE: Full energy storage capacity of the battery. The attribute shall be a positive value.
    batteryState: The current state of the battery (charging, full, etc.).
    storedE: Amount of energy currently stored. The attribute shall be a positive value or zero and lower than
      BatteryUnit.ratedE.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ratedE: float = 0.0  # Type #RealEnergy in CIM
    batteryState: Optional[str] = None  # Type M:1..1 in CIM
    storedE: float = 0.0  # Type #RealEnergy in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=BatteryUnit\n"
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
            "ratedE": [
                self.profiles.EQ.value,
            ],
            "batteryState": [
                self.profiles.SSH.value,
            ],
            "storedE": [
                self.profiles.SSH.value,
            ],
        }
