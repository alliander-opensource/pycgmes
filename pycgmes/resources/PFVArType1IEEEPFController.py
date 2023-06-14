"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PFVArControllerType1Dynamics import PFVArControllerType1Dynamics


@dataclass(config=DataclassConfig)
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

        return "\n".join(
            ["class=PFVArType1IEEEPFController"]
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
            "ovex": [
                Profile.DY.value,
            ],
            "tpfc": [
                Profile.DY.value,
            ],
            "vitmin": [
                Profile.DY.value,
            ],
            "vpf": [
                Profile.DY.value,
            ],
            "vpfcbw": [
                Profile.DY.value,
            ],
            "vpfref": [
                Profile.DY.value,
            ],
            "vvtmax": [
                Profile.DY.value,
            ],
            "vvtmin": [
                Profile.DY.value,
            ],
        }
