"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
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

    ratedE: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    batteryState: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.SSH,
        ],
    )

    storedE: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SSH,
        }
