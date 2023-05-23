"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .EnergyConnection import EnergyConnection


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=EnergySource\n"
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
                self.profiles.EQ.value,
                self.profiles.SC.value,
                self.profiles.SSH.value,
            ],
            # Attributes
            "EnergySchedulingType": [
                self.profiles.EQ.value,
            ],
            "nominalVoltage": [
                self.profiles.EQ.value,
            ],
            "pMin": [
                self.profiles.EQ.value,
            ],
            "pMax": [
                self.profiles.EQ.value,
            ],
            "r": [
                self.profiles.SC.value,
            ],
            "r0": [
                self.profiles.SC.value,
            ],
            "rn": [
                self.profiles.SC.value,
            ],
            "x": [
                self.profiles.SC.value,
            ],
            "x0": [
                self.profiles.SC.value,
            ],
            "xn": [
                self.profiles.SC.value,
            ],
            "activePower": [
                self.profiles.SSH.value,
            ],
            "reactivePower": [
                self.profiles.SSH.value,
            ],
            "voltageAngle": [
                self.profiles.SSH.value,
            ],
            "voltageMagnitude": [
                self.profiles.SSH.value,
            ],
        }
