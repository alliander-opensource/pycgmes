"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PowerSystemResource import PowerSystemResource


@dataclass(config=DataclassConfig)
class HydroPowerPlant(PowerSystemResource):
    """
    A hydro power station which can generate or pump. When generating, the generator turbines receive water from an
      upper reservoir. When pumping, the pumps receive their water from a lower reservoir.

    HydroGeneratingUnits: The hydro generating unit belongs to a hydro power plant.
    hydroPlantStorageType: The type of hydro power plant water storage.
    HydroPumps: The hydro pump may be a member of a pumped storage plant or a pump for distributing water.
    """

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # HydroGeneratingUnits : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    hydroPlantStorageType: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:0..n in CIM  # pylint: disable-next=line-too-long
    # HydroPumps : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
