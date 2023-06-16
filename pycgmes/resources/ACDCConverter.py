"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ConductingEquipment import ConductingEquipment


@dataclass(config=DataclassConfig)
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

        return "\n".join(
            ["class=ACDCConverter"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.SV.value,
                Profile.SSH.value,
                Profile.DY.value,
            ],
            # Attributes
            "baseS": [
                Profile.EQ.value,
            ],
            "idleLoss": [
                Profile.EQ.value,
            ],
            "maxUdc": [
                Profile.EQ.value,
            ],
            "minUdc": [
                Profile.EQ.value,
            ],
            "numberOfValves": [
                Profile.EQ.value,
            ],
            "ratedUdc": [
                Profile.EQ.value,
            ],
            "resistiveLoss": [
                Profile.EQ.value,
            ],
            "switchingLoss": [
                Profile.EQ.value,
            ],
            "valveU0": [
                Profile.EQ.value,
            ],
            "maxP": [
                Profile.EQ.value,
            ],
            "minP": [
                Profile.EQ.value,
            ],
            "PccTerminal": [
                Profile.EQ.value,
            ],
            "DCTerminals": [
                Profile.EQ.value,
            ],
            "idc": [
                Profile.SV.value,
            ],
            "poleLossP": [
                Profile.SV.value,
            ],
            "uc": [
                Profile.SV.value,
            ],
            "udc": [
                Profile.SV.value,
            ],
            "p": [
                Profile.SSH.value,
            ],
            "q": [
                Profile.SSH.value,
            ],
            "targetPpcc": [
                Profile.SSH.value,
            ],
            "targetUdc": [
                Profile.SSH.value,
            ],
        }
