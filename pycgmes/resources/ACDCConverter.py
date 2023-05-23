"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .ConductingEquipment import ConductingEquipment


@dataclass
class ACDCConverter(ConductingEquipment):
    """
    A unit with valves for three phases, together with unit control equipment, essential protective and switching
      devices, DC storage capacitors, phase reactors and auxiliaries, if any, used for conversion.

    baseS: Base apparent power of the converter pole. The attribute shall be a positive value.
    idleLoss: Active power loss in pole at no power transfer. It is converter`s configuration data used in power flow.
      The attribute shall be a positive value.
    maxUdc: The maximum voltage on the DC side at which the converter should operate. It is converter`s configuration
      data used in power flow. The attribute shall be a positive value.
    minUdc: The minimum voltage on the DC side at which the converter should operate. It is converter`s configuration
      data used in power flow. The attribute shall be a positive value.
    numberOfValves: Number of valves in the converter. Used in loss calculations.
    ratedUdc: Rated converter DC voltage, also called UdN. The attribute shall be a positive value. It is converter`s
      configuration data used in power flow. For instance a bipolar HVDC link with value  200 kV has a
      400kV difference between the dc lines.
    resistiveLoss: It is converter`s configuration data used in power flow. Refer to poleLossP. The attribute shall be a
      positive value.
    switchingLoss: Switching losses, relative to the base apparent power `baseS`. Refer to poleLossP. The attribute
      shall be a positive value.
    valveU0: Valve threshold voltage, also called Uvalve. Forward voltage drop when the valve is conducting. Used in
      loss calculations, i.e. the switchLoss depend on numberOfValves * valveU0.
    maxP: Maximum active power limit. The value is overwritten by values of VsCapabilityCurve, if present.
    minP: Minimum active power limit. The value is overwritten by values of VsCapabilityCurve, if present.
    PccTerminal: Point of common coupling terminal for this converter DC side. It is typically the terminal on the power
      transformer (or switch) closest to the AC network.
    DCTerminals: A DC converter have DC converter terminals. A converter has two DC converter terminals.
    idc: Converter DC current, also called Id. It is converter`s state variable, result from power flow.
    poleLossP: The active power loss at a DC Pole  = idleLoss + switchingLoss*|Idc| + resitiveLoss*Idc^2. For lossless
      operation Pdc=Pac. For rectifier operation with losses Pdc=Pac-lossP. For inverter operation with
      losses Pdc=Pac+lossP. It is converter`s state variable used in power flow. The attribute shall be a
      positive value.
    uc: Line-to-line converter voltage, the voltage at the AC side of the valve. It is converter`s state variable,
      result from power flow. The attribute shall be a positive value.
    udc: Converter voltage at the DC side, also called Ud. It is converter`s state variable, result from power flow. The
      attribute shall be a positive value.
    p: Active power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out
      from a node. Starting value for a steady state solution in the case a simplified power flow model is used.
    q: Reactive power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out
      from a node. Starting value for a steady state solution in the case a simplified power flow model is used.
    targetPpcc: Real power injection target in AC grid, at point of common coupling.  Load sign convention is used, i.e.
      positive sign means flow out from a node.
    targetUdc: Target value for DC voltage magnitude. The attribute shall be a positive value.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    baseS: float = 0.0  # Type #ApparentPower in CIM
    idleLoss: float = 0.0  # Type #ActivePower in CIM
    maxUdc: float = 0.0  # Type #Voltage in CIM
    minUdc: float = 0.0  # Type #Voltage in CIM
    numberOfValves: int = 0  # Type #Integer in CIM
    ratedUdc: float = 0.0  # Type #Voltage in CIM
    resistiveLoss: float = 0.0  # Type #Resistance in CIM
    switchingLoss: float = 0.0  # Type #ActivePowerPerCurrentFlow in CIM
    valveU0: float = 0.0  # Type #Voltage in CIM
    maxP: float = 0.0  # Type #ActivePower in CIM
    minP: float = 0.0  # Type #ActivePower in CIM
    PccTerminal: Optional[str] = None  # Type M:0..1 in CIM
    # *Association not used*
    # DCTerminals : list = field(default_factory=list)  # Type M:0..n in CIM
    idc: float = 0.0  # Type #CurrentFlow in CIM
    poleLossP: float = 0.0  # Type #ActivePower in CIM
    uc: float = 0.0  # Type #Voltage in CIM
    udc: float = 0.0  # Type #Voltage in CIM
    p: float = 0.0  # Type #ActivePower in CIM
    q: float = 0.0  # Type #ReactivePower in CIM
    targetPpcc: float = 0.0  # Type #ActivePower in CIM
    targetUdc: float = 0.0  # Type #Voltage in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ACDCConverter\n"
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
                self.profiles.SV.value,
                self.profiles.SSH.value,
                self.profiles.DY.value,
            ],
            # Attributes
            "baseS": [
                self.profiles.EQ.value,
            ],
            "idleLoss": [
                self.profiles.EQ.value,
            ],
            "maxUdc": [
                self.profiles.EQ.value,
            ],
            "minUdc": [
                self.profiles.EQ.value,
            ],
            "numberOfValves": [
                self.profiles.EQ.value,
            ],
            "ratedUdc": [
                self.profiles.EQ.value,
            ],
            "resistiveLoss": [
                self.profiles.EQ.value,
            ],
            "switchingLoss": [
                self.profiles.EQ.value,
            ],
            "valveU0": [
                self.profiles.EQ.value,
            ],
            "maxP": [
                self.profiles.EQ.value,
            ],
            "minP": [
                self.profiles.EQ.value,
            ],
            "PccTerminal": [
                self.profiles.EQ.value,
            ],
            "DCTerminals": [
                self.profiles.EQ.value,
            ],
            "idc": [
                self.profiles.SV.value,
            ],
            "poleLossP": [
                self.profiles.SV.value,
            ],
            "uc": [
                self.profiles.SV.value,
            ],
            "udc": [
                self.profiles.SV.value,
            ],
            "p": [
                self.profiles.SSH.value,
            ],
            "q": [
                self.profiles.SSH.value,
            ],
            "targetPpcc": [
                self.profiles.SSH.value,
            ],
            "targetUdc": [
                self.profiles.SSH.value,
            ],
        }
