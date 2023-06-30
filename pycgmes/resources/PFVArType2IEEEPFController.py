"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from pydantic import Field
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

    pfref: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vref: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vclmt: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ki: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vs: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    exlon: bool = Field(
        default=False,
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
