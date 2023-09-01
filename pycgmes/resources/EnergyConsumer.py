"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .EnergyConnection import EnergyConnection


@dataclass(config=DataclassConfig)
class EnergyConsumer(EnergyConnection):
    """
    Generic user of energy - a  point of consumption on the power system model. EnergyConsumer.pfixed, .qfixed,
      .pfixedPct and .qfixedPct have meaning only if there is no LoadResponseCharacteristic associated with
      EnergyConsumer or if LoadResponseCharacteristic.exponentModel is set to False.

    pfixed: Active power of the load that is a fixed quantity and does not vary as load group value varies. Load sign
      convention is used, i.e. positive sign means flow out from a node.
    pfixedPct: Fixed active power as a percentage of load group fixed active power. Used to represent the time-varying
      components.  Load sign convention is used, i.e. positive sign means flow out from a node.
    qfixed: Reactive power of the load that is a fixed quantity and does not vary as load group value varies. Load sign
      convention is used, i.e. positive sign means flow out from a node.
    qfixedPct: Fixed reactive power as a percentage of load group fixed reactive power. Used to represent the time-
      varying components.  Load sign convention is used, i.e. positive sign means flow out from a node.
    LoadResponse: The load response characteristic of this load.  If missing, this load is assumed to be constant power.
    p: Active power of the load. Load sign convention is used, i.e. positive sign means flow out from a node. For
      voltage dependent loads the value is at rated voltage. Starting value for a steady state solution.
    q: Reactive power of the load. Load sign convention is used, i.e. positive sign means flow out from a node. For
      voltage dependent loads the value is at rated voltage. Starting value for a steady state solution.
    LoadDynamics: Load dynamics model used to describe dynamic behaviour of this energy consumer.
    """

    pfixed: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    pfixedPct: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    qfixed: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    qfixedPct: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    LoadResponse: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    p: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    q: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    LoadDynamics: Optional[str] = Field(
        default=None,
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
            Profile.EQ,
            Profile.SSH,
            Profile.DY,
        }
