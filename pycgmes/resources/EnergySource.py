"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .EnergyConnection import EnergyConnection


@dataclass(config=DataclassConfig)
class EnergySource(EnergyConnection):
    """
    A generic equivalent for an energy supplier on a transmission or distribution voltage level.

    EnergySchedulingType: Energy Scheduling Type of an Energy Source.
    nominalVoltage: Phase-to-phase nominal voltage.
    pMin: This is the minimum active power that can be produced by the source. Load sign convention is used, i.e.
      positive sign means flow out from a TopologicalNode (bus) into the conducting equipment.
    pMax: This is the maximum active power that can be produced by the source. Load sign convention is used, i.e.
      positive sign means flow out from a TopologicalNode (bus) into the conducting equipment.
    r: Positive sequence Thevenin resistance.
    r0: Zero sequence Thevenin resistance.
    rn: Negative sequence Thevenin resistance.
    x: Positive sequence Thevenin reactance.
    x0: Zero sequence Thevenin reactance.
    xn: Negative sequence Thevenin reactance.
    activePower: High voltage source active injection. Load sign convention is used, i.e. positive sign means flow out
      from a node. Starting value for steady state solutions.
    reactivePower: High voltage source reactive injection. Load sign convention is used, i.e. positive sign means flow
      out from a node. Starting value for steady state solutions.
    voltageAngle: Phase angle of a-phase open circuit used when voltage characteristics need to be imposed at the node
      associated with the terminal of the energy source, such as when voltages and angles from the
      transmission level are used as input to the distribution network. The attribute shall be a
      positive value or zero.
    voltageMagnitude: Phase-to-phase open circuit voltage magnitude used when voltage characteristics need to be imposed
      at the node associated with the terminal of the energy source, such as when voltages and
      angles from the transmission level are used as input to the distribution network. The
      attribute shall be a positive value or zero.
    """

    EnergySchedulingType: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    nominalVoltage: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    pMin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    pMax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.EQ,
        ],
    )

    r: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    r0: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    rn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    x: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    x0: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    xn: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SC,
        ],
    )

    activePower: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    reactivePower: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    voltageAngle: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
        ],
    )

    voltageMagnitude: float = Field(
        default=0.0,
        in_profiles=[
            Profile.SSH,
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
            Profile.SC,
            Profile.SSH,
        }
