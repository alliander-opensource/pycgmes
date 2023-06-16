"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .LoadDynamics import LoadDynamics


@dataclass(config=DataclassConfig)
class LoadGenericNonLinear(LoadDynamics):
    """
    Generic non-linear dynamic (GNLD) load. This model can be used in mid-term and long-term voltage stability
      simulations (i.e., to study voltage collapse), as it can replace a more detailed representation of aggregate
      load, including induction motors, thermostatically controlled and static loads.

    genericNonLinearLoadModelType: Type of generic non-linear load model.
    tp: Time constant of lag function of active power (TP) (> 0).
    tq: Time constant of lag function of reactive power (TQ) (> 0).
    ls: Steady state voltage index for active power (LS).
    lt: Transient voltage index for active power (LT).
    bs: Steady state voltage index for reactive power (BS).
    bt: Transient voltage index for reactive power (BT).
    """

    genericNonLinearLoadModelType: Optional[str] = None  # Type M:1..1 in CIM
    tp: int = 0  # Type #Seconds in CIM
    tq: int = 0  # Type #Seconds in CIM
    ls: float = 0.0  # Type #Float in CIM
    lt: float = 0.0  # Type #Float in CIM
    bs: float = 0.0  # Type #Float in CIM
    bt: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=LoadGenericNonLinear"]
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
                Profile.DY.value,
            ],
            # Attributes
            "genericNonLinearLoadModelType": [
                Profile.DY.value,
            ],
            "tp": [
                Profile.DY.value,
            ],
            "tq": [
                Profile.DY.value,
            ],
            "ls": [
                Profile.DY.value,
            ],
            "lt": [
                Profile.DY.value,
            ],
            "bs": [
                Profile.DY.value,
            ],
            "bt": [
                Profile.DY.value,
            ],
        }
