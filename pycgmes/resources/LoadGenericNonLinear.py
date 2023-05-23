"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .LoadDynamics import LoadDynamics


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    genericNonLinearLoadModelType: Optional[str] = None  # Type M:1..1 in CIM
    tp: int = 0  # Type #Seconds in CIM
    tq: int = 0  # Type #Seconds in CIM
    ls: float = 0.0  # Type #Float in CIM
    lt: float = 0.0  # Type #Float in CIM
    bs: float = 0.0  # Type #Float in CIM
    bt: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=LoadGenericNonLinear\n"
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
                self.profiles.DY.value,
            ],
            # Attributes
            "genericNonLinearLoadModelType": [
                self.profiles.DY.value,
            ],
            "tp": [
                self.profiles.DY.value,
            ],
            "tq": [
                self.profiles.DY.value,
            ],
            "ls": [
                self.profiles.DY.value,
            ],
            "lt": [
                self.profiles.DY.value,
            ],
            "bs": [
                self.profiles.DY.value,
            ],
            "bt": [
                self.profiles.DY.value,
            ],
        }
