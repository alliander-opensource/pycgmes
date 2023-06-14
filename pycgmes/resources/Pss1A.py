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
class Pss1A(PowerSystemStabilizerDynamics):
    """
    Single input power system stabilizer. It is a modified version in order to allow representation of various vendors'
      implementations on PSS type 1A.

    inputSignalType: Type of input signal (rotorAngularFrequencyDeviation, busFrequencyDeviation,
      generatorElectricalPower, generatorAcceleratingPower, busVoltage, or busVoltageDerivative).
    a1: Notch filter parameter (A1).
    a2: Notch filter parameter (A2).
    t1: Lead/lag time constant (T1) (>= 0).
    t2: Lead/lag time constant (T2) (>= 0).
    t3: Lead/lag time constant (T3) (>= 0).
    t4: Lead/lag time constant (T4) (>= 0).
    t5: Washout time constant (T5) (>= 0).
    t6: Transducer time constant (T6) (>= 0).
    ks: Stabilizer gain (Ks).
    vrmax: Maximum stabilizer output (Vrmax) (> Pss1A.vrmin).
    vrmin: Minimum stabilizer output (Vrmin) (< Pss1A.vrmax).
    vcu: Stabilizer input cutoff threshold (Vcu).
    vcl: Stabilizer input cutoff threshold (Vcl).
    a3: Notch filter parameter (A3).
    a4: Notch filter parameter (A4).
    a5: Notch filter parameter (A5).
    a6: Notch filter parameter (A6).
    a7: Notch filter parameter (A7).
    a8: Notch filter parameter (A8).
    kd: Selector (Kd).  true = e-sTdelay used false = e-sTdelay not used.
    tdelay: Time constant (Tdelay) (>= 0).
    """

    inputSignalType: Optional[str] = None  # Type M:1..1 in CIM
    a1: float = 0.0  # Type #PU in CIM
    a2: float = 0.0  # Type #PU in CIM
    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    t4: int = 0  # Type #Seconds in CIM
    t5: int = 0  # Type #Seconds in CIM
    t6: int = 0  # Type #Seconds in CIM
    ks: float = 0.0  # Type #PU in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    vcu: float = 0.0  # Type #PU in CIM
    vcl: float = 0.0  # Type #PU in CIM
    a3: float = 0.0  # Type #PU in CIM
    a4: float = 0.0  # Type #PU in CIM
    a5: float = 0.0  # Type #PU in CIM
    a6: float = 0.0  # Type #PU in CIM
    a7: float = 0.0  # Type #PU in CIM
    a8: float = 0.0  # Type #PU in CIM
    kd: bool = False  # Type #Boolean in CIM
    tdelay: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=Pss1A"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "inputSignalType": [
                Profile.DY.value,
            ],
            "a1": [
                Profile.DY.value,
            ],
            "a2": [
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
            "ks": [
                Profile.DY.value,
            ],
            "vrmax": [
                Profile.DY.value,
            ],
            "vrmin": [
                Profile.DY.value,
            ],
            "vcu": [
                Profile.DY.value,
            ],
            "vcl": [
                Profile.DY.value,
            ],
            "a3": [
                Profile.DY.value,
            ],
            "a4": [
                Profile.DY.value,
            ],
            "a5": [
                Profile.DY.value,
            ],
            "a6": [
                Profile.DY.value,
            ],
            "a7": [
                Profile.DY.value,
            ],
            "a8": [
                Profile.DY.value,
            ],
            "kd": [
                Profile.DY.value,
            ],
            "tdelay": [
                Profile.DY.value,
            ],
        }
