"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .RegulatingCondEq import RegulatingCondEq


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=PowerElectronicsConnection\n"
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
                self.profiles.DY.value,
            ],
            # Attributes
            "maxQ": [
                self.profiles.EQ.value,
            ],
            "minQ": [
                self.profiles.EQ.value,
            ],
            "ratedS": [
                self.profiles.EQ.value,
            ],
            "ratedU": [
                self.profiles.EQ.value,
            ],
            "PowerElectronicsUnit": [
                self.profiles.EQ.value,
            ],
            "p": [
                self.profiles.SSH.value,
            ],
            "q": [
                self.profiles.SSH.value,
            ],
            "WindTurbineType3or4Dynamics": [
                self.profiles.DY.value,
            ],
        }
