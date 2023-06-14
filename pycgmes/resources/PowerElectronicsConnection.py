"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
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

    maxQ: float = 0.0  # Type #ReactivePower in CIM
    minQ: float = 0.0  # Type #ReactivePower in CIM
    ratedS: float = 0.0  # Type #ApparentPower in CIM
    ratedU: float = 0.0  # Type #Voltage in CIM
    PowerElectronicsUnit: Optional[str] = None  # Type M:0..1 in CIM
    p: float = 0.0  # Type #ActivePower in CIM
    q: float = 0.0  # Type #ReactivePower in CIM
    # *Association not used*
    # WindTurbineType3or4Dynamics : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PowerElectronicsConnection"]
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
                Profile.DY.value,
            ],
            # Attributes
            "maxQ": [
                Profile.EQ.value,
            ],
            "minQ": [
                Profile.EQ.value,
            ],
            "ratedS": [
                Profile.EQ.value,
            ],
            "ratedU": [
                Profile.EQ.value,
            ],
            "PowerElectronicsUnit": [
                Profile.EQ.value,
            ],
            "p": [
                Profile.SSH.value,
            ],
            "q": [
                Profile.SSH.value,
            ],
            "WindTurbineType3or4Dynamics": [
                Profile.DY.value,
            ],
        }
