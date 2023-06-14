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
class Pss2ST(PowerSystemStabilizerDynamics):
    """
    PTI microprocessor-based stabilizer type 1.

    inputSignal1Type: Type of input signal #1 (rotorAngularFrequencyDeviation, busFrequencyDeviation,
      generatorElectricalPower, generatorAcceleratingPower, busVoltage, or busVoltageDerivative -
      shall be different than Pss2ST.inputSignal2Type).  Typical value =
      rotorAngularFrequencyDeviation.
    inputSignal2Type: Type of input signal #2 (rotorAngularFrequencyDeviation, busFrequencyDeviation,
      generatorElectricalPower, generatorAcceleratingPower, busVoltage, or busVoltageDerivative -
      shall be different than Pss2ST.inputSignal1Type).  Typical value = busVoltageDerivative.
    k1: Gain (K1).
    k2: Gain (K2).
    t1: Time constant (T1) (>= 0).
    t2: Time constant (T2) (>= 0).
    t3: Time constant (T3) (>= 0).
    t4: Time constant (T4) (>= 0).
    t5: Time constant (T5) (>= 0).
    t6: Time constant (T6) (>= 0).
    t7: Time constant (T7) (>= 0).
    t8: Time constant (T8) (>= 0).
    t9: Time constant (T9) (>= 0).
    t10: Time constant (T10) (>= 0).
    lsmax: Limiter (LSMAX) (> Pss2ST.lsmin).
    lsmin: Limiter (LSMIN) (< Pss2ST.lsmax).
    vcu: Cutoff limiter (VCU).
    vcl: Cutoff limiter (VCL).
    """

    inputSignal1Type: Optional[str] = None  # Type M:1..1 in CIM
    inputSignal2Type: Optional[str] = None  # Type M:1..1 in CIM
    k1: float = 0.0  # Type #PU in CIM
    k2: float = 0.0  # Type #PU in CIM
    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    t4: int = 0  # Type #Seconds in CIM
    t5: int = 0  # Type #Seconds in CIM
    t6: int = 0  # Type #Seconds in CIM
    t7: int = 0  # Type #Seconds in CIM
    t8: int = 0  # Type #Seconds in CIM
    t9: int = 0  # Type #Seconds in CIM
    t10: int = 0  # Type #Seconds in CIM
    lsmax: float = 0.0  # Type #PU in CIM
    lsmin: float = 0.0  # Type #PU in CIM
    vcu: float = 0.0  # Type #PU in CIM
    vcl: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=Pss2ST"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "k2": [
                Profile.DY.value,
            ],
            "t1": [
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
            "t9": [
                Profile.DY.value,
            ],
            "t10": [
                Profile.DY.value,
            ],
            "lsmax": [
                Profile.DY.value,
            ],
            "lsmin": [
                Profile.DY.value,
            ],
            "vcu": [
                Profile.DY.value,
            ],
            "vcl": [
                Profile.DY.value,
            ],
        }
