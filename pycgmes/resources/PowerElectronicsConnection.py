"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .RegulatingCondEq import RegulatingCondEq


@dataclass(config=DataclassConfig)
class PowerElectronicsConnection(RegulatingCondEq):
    """
    A connection to the AC network for energy production or consumption that uses power electronics rather than rotating
      machines.

    maxQ: Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.
    minQ: Minimum reactive power limit for the unit. This is the minimum (nameplate) limit for the unit.
    ratedS: Nameplate apparent power rating for the unit. The attribute shall have a positive value.
    ratedU: Rated voltage (nameplate data, Ur in IEC 60909-0). It is primarily used for short circuit data exchange
      according to IEC 60909. The attribute shall be a positive value.
    PowerElectronicsUnit: An AC network connection may have several power electronics units connecting through it.
    p: Active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting
      value for a steady state solution.
    q: Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting
      value for a steady state solution.
    WindTurbineType3or4Dynamics: The wind turbine type 3 or type 4 dynamics model associated with this power electronics
      connection.
    """

    maxQ: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    minQ: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    ratedS: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    ratedU: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    PowerElectronicsUnit: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    p: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    q: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # WindTurbineType3or4Dynamics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SSH,
            Profile.DY,
        }
