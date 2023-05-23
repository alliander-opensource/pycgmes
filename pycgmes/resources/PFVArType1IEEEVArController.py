"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .PFVArControllerType1Dynamics import PFVArControllerType1Dynamics


@dataclass
class PFVArType1IEEEVArController(PFVArControllerType1Dynamics):
    """
    IEEE VAR controller type 1 which operates by moving the voltage reference directly. Reference: IEEE 421.5-2005,
      11.3.

    tvarc: Var controller time delay (TVARC) (>= 0).  Typical value = 5.
    vvar: Synchronous machine power factor (VVAR).
    vvarcbw: Var controller deadband (VVARC_BW).  Typical value = 0,02.
    vvarref: Var controller reference (VVARREF).
    vvtmax: Maximum machine terminal voltage needed for pf/VAr controller to be enabled (VVTMAX) (>
      PVFArType1IEEEVArController.vvtmin).
    vvtmin: Minimum machine terminal voltage needed to enable pf/var controller (VVTMIN) (<
      PVFArType1IEEEVArController.vvtmax).
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    tvarc: int = 0  # Type #Seconds in CIM
    vvar: float = 0.0  # Type #PU in CIM
    vvarcbw: float = 0.0  # Type #Float in CIM
    vvarref: float = 0.0  # Type #PU in CIM
    vvtmax: float = 0.0  # Type #PU in CIM
    vvtmin: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PFVArType1IEEEVArController\n"
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
            "tvarc": [
                self.profiles.DY.value,
            ],
            "vvar": [
                self.profiles.DY.value,
            ],
            "vvarcbw": [
                self.profiles.DY.value,
            ],
            "vvarref": [
                self.profiles.DY.value,
            ],
            "vvtmax": [
                self.profiles.DY.value,
            ],
            "vvtmin": [
                self.profiles.DY.value,
            ],
        }
