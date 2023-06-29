"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PFVArControllerType1Dynamics import PFVArControllerType1Dynamics


@dataclass(config=DataclassConfig)
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

    tvarc: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vvar: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vvarcbw: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vvarref: float = Field(
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
