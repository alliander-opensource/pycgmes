"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .PFVArControllerType2Dynamics import PFVArControllerType2Dynamics


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    pfref: float = 0.0  # Type #PU in CIM
    vref: float = 0.0  # Type #PU in CIM
    vclmt: float = 0.0  # Type #PU in CIM
    kp: float = 0.0  # Type #PU in CIM
    ki: float = 0.0  # Type #PU in CIM
    vs: float = 0.0  # Type #Float in CIM
    exlon: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PFVArType2IEEEPFController\n"
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
            "pfref": [
                self.profiles.DY.value,
            ],
            "vref": [
                self.profiles.DY.value,
            ],
            "vclmt": [
                self.profiles.DY.value,
            ],
            "kp": [
                self.profiles.DY.value,
            ],
            "ki": [
                self.profiles.DY.value,
            ],
            "vs": [
                self.profiles.DY.value,
            ],
            "exlon": [
                self.profiles.DY.value,
            ],
        }
