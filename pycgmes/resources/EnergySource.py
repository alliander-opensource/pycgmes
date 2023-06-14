"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
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

    EnergySchedulingType: Optional[str] = None  # Type M:0..1 in CIM
    nominalVoltage: float = 0.0  # Type #Voltage in CIM
    pMin: float = 0.0  # Type #ActivePower in CIM
    pMax: float = 0.0  # Type #ActivePower in CIM
    r: float = 0.0  # Type #Resistance in CIM
    r0: float = 0.0  # Type #Resistance in CIM
    rn: float = 0.0  # Type #Resistance in CIM
    x: float = 0.0  # Type #Reactance in CIM
    x0: float = 0.0  # Type #Reactance in CIM
    xn: float = 0.0  # Type #Reactance in CIM
    activePower: float = 0.0  # Type #ActivePower in CIM
    reactivePower: float = 0.0  # Type #ReactivePower in CIM
    voltageAngle: float = 0.0  # Type #AngleRadians in CIM
    voltageMagnitude: float = 0.0  # Type #Voltage in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=EnergySource"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.EQ.value,
                Profile.SC.value,
                Profile.SSH.value,
            ],
            # Attributes
            "EnergySchedulingType": [
                Profile.EQ.value,
            ],
            "nominalVoltage": [
                Profile.EQ.value,
            ],
            "pMin": [
                Profile.EQ.value,
            ],
            "pMax": [
                Profile.EQ.value,
            ],
            "r": [
                Profile.SC.value,
            ],
            "r0": [
                Profile.SC.value,
            ],
            "rn": [
                Profile.SC.value,
            ],
            "x": [
                Profile.SC.value,
            ],
            "x0": [
                Profile.SC.value,
            ],
            "xn": [
                Profile.SC.value,
            ],
            "activePower": [
                Profile.SSH.value,
            ],
            "reactivePower": [
                Profile.SSH.value,
            ],
            "voltageAngle": [
                Profile.SSH.value,
            ],
            "voltageMagnitude": [
                Profile.SSH.value,
            ],
        }
