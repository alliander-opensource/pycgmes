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

        return "\n".join(
            ["class=RotatingMachine"]
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
                Profile.SC.value,
                Profile.SSH.value,
                Profile.DY.value,
            ],
            # Attributes
            "GeneratingUnit": [
                Profile.EQ.value,
            ],
            "HydroPump": [
                Profile.EQ.value,
            ],
            "ratedPowerFactor": [
                Profile.EQ.value,
            ],
            "ratedS": [
                Profile.EQ.value,
            ],
            "ratedU": [
                Profile.EQ.value,
            ],
            "p": [
                Profile.SSH.value,
            ],
            "q": [
                Profile.SSH.value,
            ],
        }
