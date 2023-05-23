"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .RegulatingCondEq import RegulatingCondEq


@dataclass
class RotatingMachine(RegulatingCondEq):
    """
    A rotating machine which may be used as a generator or motor.

    GeneratingUnit: A synchronous machine may operate as a generator and as such becomes a member of a generating unit.
    HydroPump: The synchronous machine drives the turbine which moves the water from a low elevation to a higher
      elevation. The direction of machine rotation for pumping may or may not be the same as for
      generating.
    ratedPowerFactor: Power factor (nameplate data). It is primarily used for short circuit data exchange according to
      IEC 60909. The attribute cannot be a negative value.
    ratedS: Nameplate apparent power rating for the unit. The attribute shall have a positive value.
    ratedU: Rated voltage (nameplate data, Ur in IEC 60909-0). It is primarily used for short circuit data exchange
      according to IEC 60909. The attribute shall be a positive value.
    p: Active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting
      value for a steady state solution.
    q: Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting
      value for a steady state solution.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    GeneratingUnit: Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # HydroPump : Optional[str] = None  # Type M:0..1 in CIM
    ratedPowerFactor: float = 0.0  # Type #Float in CIM
    ratedS: float = 0.0  # Type #ApparentPower in CIM
    ratedU: float = 0.0  # Type #Voltage in CIM
    p: float = 0.0  # Type #ActivePower in CIM
    q: float = 0.0  # Type #ReactivePower in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=RotatingMachine\n"
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
                self.profiles.SC.value,
                self.profiles.SSH.value,
                self.profiles.DY.value,
            ],
            # Attributes
            "GeneratingUnit": [
                self.profiles.EQ.value,
            ],
            "HydroPump": [
                self.profiles.EQ.value,
            ],
            "ratedPowerFactor": [
                self.profiles.EQ.value,
            ],
            "ratedS": [
                self.profiles.EQ.value,
            ],
            "ratedU": [
                self.profiles.EQ.value,
            ],
            "p": [
                self.profiles.SSH.value,
            ],
            "q": [
                self.profiles.SSH.value,
            ],
        }
