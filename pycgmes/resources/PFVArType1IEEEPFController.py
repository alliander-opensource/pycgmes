"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .PFVArControllerType1Dynamics import PFVArControllerType1Dynamics


@dataclass
class PFVArType1IEEEPFController(PFVArControllerType1Dynamics):
    """
    IEEE PF controller type 1 which operates by moving the voltage reference directly. Reference: IEEE 421.5-2005, 11.2.

    ovex: Overexcitation Flag (OVEX) true = overexcited false = underexcited.
    tpfc: PF controller time delay (TPFC) (>= 0).  Typical value = 5.
    vitmin: Minimum machine terminal current needed to enable pf/var controller (VITMIN).
    vpf: Synchronous machine power factor (VPF).
    vpfcbw: PF controller deadband (VPFC_BW).  Typical value = 0,05.
    vpfref: PF controller reference (VPFREF).
    vvtmax: Maximum machine terminal voltage needed for pf/var controller to be enabled (VVTMAX) (>
      PFVArType1IEEEPFController.vvtmin).
    vvtmin: Minimum machine terminal voltage needed to enable pf/var controller (VVTMIN) (<
      PFVArType1IEEEPFController.vvtmax).
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ovex: bool = False  # Type #Boolean in CIM
    tpfc: int = 0  # Type #Seconds in CIM
    vitmin: float = 0.0  # Type #PU in CIM
    vpf: float = 0.0  # Type #PU in CIM
    vpfcbw: float = 0.0  # Type #Float in CIM
    vpfref: float = 0.0  # Type #PU in CIM
    vvtmax: float = 0.0  # Type #PU in CIM
    vvtmin: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=PFVArType1IEEEPFController\n"
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
            "ovex": [
                self.profiles.DY.value,
            ],
            "tpfc": [
                self.profiles.DY.value,
            ],
            "vitmin": [
                self.profiles.DY.value,
            ],
            "vpf": [
                self.profiles.DY.value,
            ],
            "vpfcbw": [
                self.profiles.DY.value,
            ],
            "vpfref": [
                self.profiles.DY.value,
            ],
            "vvtmax": [
                self.profiles.DY.value,
            ],
            "vvtmin": [
                self.profiles.DY.value,
            ],
        }
