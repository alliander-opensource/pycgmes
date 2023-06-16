"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PFVArControllerType2Dynamics import PFVArControllerType2Dynamics


@dataclass(config=DataclassConfig)
class PFVArType2IEEEPFController(PFVArControllerType2Dynamics):
    """
    IEEE PF controller type 2 which is a summing point type controller making up the outside loop of a two-loop system.
      This controller is implemented as a slow PI type controller. The voltage regulator forms the inner loop and is
      implemented as a fast controller. Reference: IEEE 421.5-2005, 11.4.

    pfref: Power factor reference (PFREF).
    vref: Voltage regulator reference (VREF).
    vclmt: Maximum output of the pf controller (VCLMT).  Typical value = 0,1.
    kp: Proportional gain of the pf controller (KP).  Typical value = 1.
    ki: Integral gain of the pf controller (KI).  Typical value = 1.
    vs: Generator sensing voltage (VS).
    exlon: Overexcitation or under excitation flag (EXLON) true = 1 (not in the overexcitation or underexcitation state,
      integral action is active) false = 0 (in the overexcitation or underexcitation state, so integral
      action is disabled to allow the limiter to play its role).
    """

    pfref: float = 0.0  # Type #PU in CIM
    vref: float = 0.0  # Type #PU in CIM
    vclmt: float = 0.0  # Type #PU in CIM
    kp: float = 0.0  # Type #PU in CIM
    ki: float = 0.0  # Type #PU in CIM
    vs: float = 0.0  # Type #Float in CIM
    exlon: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PFVArType2IEEEPFController"]
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
            "pfref": [
                Profile.DY.value,
            ],
            "vref": [
                Profile.DY.value,
            ],
            "vclmt": [
                Profile.DY.value,
            ],
            "kp": [
                Profile.DY.value,
            ],
            "ki": [
                Profile.DY.value,
            ],
            "vs": [
                Profile.DY.value,
            ],
            "exlon": [
                Profile.DY.value,
            ],
        }
