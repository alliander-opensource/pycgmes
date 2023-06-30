"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic import Field
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

    ovex: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    tpfc: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vitmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vpf: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vpfcbw: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vpfref: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vvtmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vvtmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
