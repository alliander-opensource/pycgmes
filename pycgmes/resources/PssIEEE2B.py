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
class PssIEEE2B(PowerSystemStabilizerDynamics):
    """
    IEEE 421.5-2005 type PSS2B power system stabilizer model. This stabilizer model is designed to represent a variety
      of dual-input stabilizers, which normally use combinations of power and speed or frequency to derive the
      stabilizing signal. Reference: IEEE 2B 421.5-2005, 8.2.

    inputSignal1Type: Type of input signal #1 (rotorAngularFrequencyDeviation, busFrequencyDeviation).  Typical value =
      rotorAngularFrequencyDeviation.
    inputSignal2Type: Type of input signal #2 (generatorElectricalPower).  Typical value = generatorElectricalPower.
    vsi1max: Input signal #1 maximum limit (Vsi1max) (> PssIEEE2B.vsi1min).  Typical value = 2.
    vsi1min: Input signal #1 minimum limit (Vsi1min) (< PssIEEE2B.vsi1max).  Typical value = -2.
    tw1: First washout on signal #1 (Tw1) (>= 0).  Typical value = 2.
    tw2: Second washout on signal #1 (Tw2) (>= 0).  Typical value = 2.
    vsi2max: Input signal #2 maximum limit (Vsi2max) (> PssIEEE2B.vsi2min).  Typical value = 2.
    vsi2min: Input signal #2 minimum limit (Vsi2min) (< PssIEEE2B.vsi2max).  Typical value = -2.
    tw3: First washout on signal #2 (Tw3) (>= 0).  Typical value = 2.
    tw4: Second washout on signal #2 (Tw4) (>= 0).  Typical value = 0.
    t1: Lead/lag time constant (T1) (>= 0).  Typical value = 0,12.
    t2: Lead/lag time constant (T2) (>= 0).  Typical value = 0,02.
    t3: Lead/lag time constant (T3) (>= 0).  Typical value = 0,3.
    t4: Lead/lag time constant (T4) (>= 0).  Typical value = 0,02.
    t6: Time constant on signal #1 (T6) (>= 0).  Typical value = 0.
    t7: Time constant on signal #2 (T7) (>= 0).  Typical value = 2.
    t8: Lead of ramp tracking filter (T8) (>= 0).  Typical value = 0,2.
    t9: Lag of ramp tracking filter (T9) (>= 0).  Typical value = 0,1.
    t10: Lead/lag time constant (T10) (>= 0).  Typical value = 0.
    t11: Lead/lag time constant (T11) (>= 0).  Typical value = 0.
    ks1: Stabilizer gain (Ks1).  Typical value = 12.
    ks2: Gain on signal #2 (Ks2).  Typical value = 0,2.
    ks3: Gain on signal #2 input before ramp-tracking filter (Ks3).  Typical value = 1.
    n: Order of ramp tracking filter (N).  Typical value = 1.
    m: Denominator order of ramp tracking filter (M).  Typical value = 5.
    vstmax: Stabilizer output maximum limit (Vstmax) (> PssIEEE2B.vstmin).  Typical value = 0,1.
    vstmin: Stabilizer output minimum limit (Vstmin) (< PssIEEE2B.vstmax).  Typical value = -0,1.
    """

    inputSignal1Type: Optional[str] = None  # Type M:1..1 in CIM
    inputSignal2Type: Optional[str] = None  # Type M:1..1 in CIM
    vsi1max: float = 0.0  # Type #PU in CIM
    vsi1min: float = 0.0  # Type #PU in CIM
    tw1: int = 0  # Type #Seconds in CIM
    tw2: int = 0  # Type #Seconds in CIM
    vsi2max: float = 0.0  # Type #PU in CIM
    vsi2min: float = 0.0  # Type #PU in CIM
    tw3: int = 0  # Type #Seconds in CIM
    tw4: int = 0  # Type #Seconds in CIM
    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    t4: int = 0  # Type #Seconds in CIM
    t6: int = 0  # Type #Seconds in CIM
    t7: int = 0  # Type #Seconds in CIM
    t8: int = 0  # Type #Seconds in CIM
    t9: int = 0  # Type #Seconds in CIM
    t10: int = 0  # Type #Seconds in CIM
    t11: int = 0  # Type #Seconds in CIM
    ks1: float = 0.0  # Type #PU in CIM
    ks2: float = 0.0  # Type #PU in CIM
    ks3: float = 0.0  # Type #PU in CIM
    n: int = 0  # Type #Integer in CIM
    m: int = 0  # Type #Integer in CIM
    vstmax: float = 0.0  # Type #PU in CIM
    vstmin: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PssIEEE2B"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "vsi1max": [
                Profile.DY.value,
            ],
            "vsi1min": [
                Profile.DY.value,
            ],
            "tw1": [
                Profile.DY.value,
            ],
            "tw2": [
                Profile.DY.value,
            ],
            "vsi2max": [
                Profile.DY.value,
            ],
            "vsi2min": [
                Profile.DY.value,
            ],
            "tw3": [
                Profile.DY.value,
            ],
            "tw4": [
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
            "t11": [
                Profile.DY.value,
            ],
            "ks1": [
                Profile.DY.value,
            ],
            "ks2": [
                Profile.DY.value,
            ],
            "ks3": [
                Profile.DY.value,
            ],
            "n": [
                Profile.DY.value,
            ],
            "m": [
                Profile.DY.value,
            ],
            "vstmax": [
                Profile.DY.value,
            ],
            "vstmin": [
                Profile.DY.value,
            ],
        }
