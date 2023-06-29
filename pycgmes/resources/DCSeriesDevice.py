"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .DCConductingEquipment import DCConductingEquipment


@dataclass(config=DataclassConfig)
class DCSeriesDevice(DCConductingEquipment):
    """
    A series device within the DC system, typically a reactor used for filtering or smoothing.  Needed for transient and
      short circuit studies.

    inductance: Inductance of the device.
    resistance: Resistance of the DC device.
    """

    inductance: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    resistance: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
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
        }
