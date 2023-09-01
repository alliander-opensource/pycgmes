"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .RegulatingCondEq import RegulatingCondEq


@dataclass(config=DataclassConfig)
class StaticVarCompensator(RegulatingCondEq):
    """
    A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown
      transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate
      in fixed MVar output mode or in voltage control mode. When in voltage control mode, the output of the SVC will
      be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC
      characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage
      setpoint, the SVC MVar output is zero.

    capacitiveRating: Capacitive reactance at maximum capacitive reactive power.  Shall always be positive.
    inductiveRating: Inductive reactance at maximum inductive reactive power.  Shall always be negative.
    slope: The characteristics slope of an SVC defines how the reactive power output changes in proportion to the
      difference between the regulated bus voltage and the voltage setpoint. The attribute shall be a
      positive value or zero.
    sVCControlMode: SVC control mode.
    voltageSetPoint: The reactive power output of the SVC is proportional to the difference between the voltage at the
      regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the
      voltage setpoint, the reactive power output is zero.
    q: Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting
      value for a steady state solution.
    StaticVarCompensatorDynamics: Static Var Compensator dynamics model used to describe dynamic behaviour of this
      Static Var Compensator.
    """

    capacitiveRating: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    inductiveRating: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    slope: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    sVCControlMode: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    voltageSetPoint: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    q: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # StaticVarCompensatorDynamics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SSH,
            Profile.DY,
        }
