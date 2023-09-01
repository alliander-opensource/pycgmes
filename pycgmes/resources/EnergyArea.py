"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .IdentifiedObject import IdentifiedObject


@dataclass(config=DataclassConfig)
class EnergyArea(IdentifiedObject):
    """
    Describes an area having energy production or consumption.  Specializations are intended to support the load
      allocation function as typically required in energy management systems or planning studies to allocate
      hypothesized load levels to individual load points for power flow analysis.  Often the energy area can be
      linked to both measured and forecast load levels.

    ControlArea: The control area specification that is used for the load forecast.
    """

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # ControlArea : Optional[str] = Field(default=None, in_profiles = [Profile.EQ, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
