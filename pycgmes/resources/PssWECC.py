"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass(config=DataclassConfig)
class PssWECC(PowerSystemStabilizerDynamics):
    """
    Dual input power system stabilizer, based on IEEE type 2, with modified output limiter defined by WECC (Western
      Electricity Coordinating Council, USA).

    inputSignal1Type: Type of input signal #1 (rotorAngularFrequencyDeviation, busFrequencyDeviation,
      generatorElectricalPower, generatorAcceleratingPower, busVoltage, or busVoltageDerivative -
      shall be different than PssWECC.inputSignal2Type).  Typical value =
      rotorAngularFrequencyDeviation.
    inputSignal2Type: Type of input signal #2 (rotorAngularFrequencyDeviation, busFrequencyDeviation,
      generatorElectricalPower, generatorAcceleratingPower, busVoltage, busVoltageDerivative -
      shall be different than PssWECC.inputSignal1Type).  Typical value = busVoltageDerivative.
    k1: Input signal 1 gain (K1).  Typical value = 1,13.
    t1: Input signal 1 transducer time constant (T1) (>= 0).  Typical value = 0,037.
    k2: Input signal 2 gain (K2).  Typical value = 0,0.
    t2: Input signal 2 transducer time constant (T2) (>= 0).  Typical value = 0,0.
    t3: Stabilizer washout time constant (T3) (>= 0).  Typical value = 9,5.
    t4: Stabilizer washout time lag constant (T4) (>= 0).  Typical value = 9,5.
    t5: Lead time constant (T5) (>= 0).  Typical value = 1,7.
    t6: Lag time constant (T6) (>= 0).  Typical value = 1,5.
    t7: Lead time constant (T7) (>= 0).  Typical value = 1,7.
    t8: Lag time constant (T8) (>= 0).  Typical value = 1,5.
    t10: Lag time constant (T10) (>= 0).  Typical value = 0.
    t9: Lead time constant (T9) (>= 0).  Typical value = 0.
    vsmax: Maximum output signal (Vsmax) (> PssWECC.vsmin). Typical value = 0,05.
    vsmin: Minimum output signal (Vsmin) (< PssWECC.vsmax).  Typical value = -0,05.
    vcu: Maximum value for voltage compensator output (VCU). Typical value = 0.
    vcl: Minimum value for voltage compensator output (VCL). Typical value = 0.
    """

    inputSignal1Type: Optional[str] = None  # Type M:1..1 in CIM
    inputSignal2Type: Optional[str] = None  # Type M:1..1 in CIM
    k1: float = 0.0  # Type #PU in CIM
    t1: int = 0  # Type #Seconds in CIM
    k2: float = 0.0  # Type #PU in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    t4: int = 0  # Type #Seconds in CIM
    t5: int = 0  # Type #Seconds in CIM
    t6: int = 0  # Type #Seconds in CIM
    t7: int = 0  # Type #Seconds in CIM
    t8: int = 0  # Type #Seconds in CIM
    t10: int = 0  # Type #Seconds in CIM
    t9: int = 0  # Type #Seconds in CIM
    vsmax: float = 0.0  # Type #PU in CIM
    vsmin: float = 0.0  # Type #PU in CIM
    vcu: float = 0.0  # Type #PU in CIM
    vcl: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PssWECC"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
                Profile.DY.value,
            ],
            # Attributes
            "inputSignal1Type": [
                Profile.DY.value,
            ],
            "inputSignal2Type": [
                Profile.DY.value,
            ],
            "k1": [
                Profile.DY.value,
            ],
            "t1": [
                Profile.DY.value,
            ],
            "k2": [
                Profile.DY.value,
            ],
            "t2": [
                Profile.DY.value,
            ],
            "t3": [
                Profile.DY.value,
            ],
            "t4": [
                Profile.DY.value,
            ],
            "t5": [
                Profile.DY.value,
            ],
            "t6": [
                Profile.DY.value,
            ],
            "t7": [
                Profile.DY.value,
            ],
            "t8": [
                Profile.DY.value,
            ],
            "t10": [
                Profile.DY.value,
            ],
            "t9": [
                Profile.DY.value,
            ],
            "vsmax": [
                Profile.DY.value,
            ],
            "vsmin": [
                Profile.DY.value,
            ],
            "vcu": [
                Profile.DY.value,
            ],
            "vcl": [
                Profile.DY.value,
            ],
        }
