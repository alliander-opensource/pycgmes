"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ACDCConverter import ACDCConverter


@dataclass(config=DataclassConfig)
class VsConverter(ACDCConverter):
    """
    DC side of the voltage source converter (VSC).

    CapabilityCurve: Capability curve of this converter.
    maxModulationIndex: The maximum quotient between the AC converter voltage (Uc) and DC voltage (Ud). A factor
      typically less than 1. It is converter`s configuration data used in power flow.
    delta: Angle between VsConverter.uv and ACDCConverter.uc. It is converter`s state variable used in power flow. The
      attribute shall be a positive value or zero.
    uv: Line-to-line voltage on the valve side of the converter transformer. It is converter`s state variable, result
      from power flow. The attribute shall be a positive value.
    droop: Droop constant. The pu value is obtained as D [kV/MW] x Sb / Ubdc. The attribute shall be a positive value.
    droopCompensation: Compensation constant. Used to compensate for voltage drop when controlling voltage at a distant
      bus. The attribute shall be a positive value.
    pPccControl: Kind of control of real power and/or DC voltage.
    qPccControl: Kind of reactive power control.
    qShare: Reactive power sharing factor among parallel converters on Uac control. The attribute shall be a positive
      value or zero.
    targetQpcc: Reactive power injection target in AC grid, at point of common coupling.  Load sign convention is used,
      i.e. positive sign means flow out from a node.
    targetUpcc: Voltage target in AC grid, at point of common coupling. The attribute shall be a positive value.
    targetPowerFactorPcc: Power factor target at the AC side, at point of common coupling. The attribute shall be a
      positive value.
    targetPhasePcc: Phase target at AC side, at point of common coupling. The attribute shall be a positive value.
    targetPWMfactor: Magnitude of pulse-modulation factor. The attribute shall be a positive value.
    VSCDynamics: Voltage source converter dynamics model used to describe dynamic behaviour of this converter.
    """

    CapabilityCurve: Optional[str] = None  # Type M:0..1 in CIM
    maxModulationIndex: float = 0.0  # Type #Float in CIM
    delta: float = 0.0  # Type #AngleDegrees in CIM
    uv: float = 0.0  # Type #Voltage in CIM
    droop: float = 0.0  # Type #PU in CIM
    droopCompensation: float = 0.0  # Type #Resistance in CIM
    pPccControl: Optional[str] = None  # Type M:1..1 in CIM
    qPccControl: Optional[str] = None  # Type M:1..1 in CIM
    qShare: float = 0.0  # Type #PerCent in CIM
    targetQpcc: float = 0.0  # Type #ReactivePower in CIM
    targetUpcc: float = 0.0  # Type #Voltage in CIM
    targetPowerFactorPcc: float = 0.0  # Type #Float in CIM
    targetPhasePcc: float = 0.0  # Type #AngleDegrees in CIM
    targetPWMfactor: float = 0.0  # Type #Float in CIM
    # *Association not used*
    # VSCDynamics : Optional[str] = None  # Type M:0..1 in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=VsConverter"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "CapabilityCurve": [
                Profile.EQ.value,
            ],
            "maxModulationIndex": [
                Profile.EQ.value,
            ],
            "delta": [
                Profile.SV.value,
            ],
            "uv": [
                Profile.SV.value,
            ],
            "droop": [
                Profile.SSH.value,
            ],
            "droopCompensation": [
                Profile.SSH.value,
            ],
            "pPccControl": [
                Profile.SSH.value,
            ],
            "qPccControl": [
                Profile.SSH.value,
            ],
            "qShare": [
                Profile.SSH.value,
            ],
            "targetQpcc": [
                Profile.SSH.value,
            ],
            "targetUpcc": [
                Profile.SSH.value,
            ],
            "targetPowerFactorPcc": [
                Profile.SSH.value,
            ],
            "targetPhasePcc": [
                Profile.SSH.value,
            ],
            "targetPWMfactor": [
                Profile.SSH.value,
            ],
            "VSCDynamics": [
                Profile.DY.value,
            ],
        }
