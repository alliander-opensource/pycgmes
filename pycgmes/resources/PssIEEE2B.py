"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
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

    inputSignal1Type: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    inputSignal2Type: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    vsi1max: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vsi1min: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tw1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tw2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vsi2max: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vsi2min: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tw3: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tw4: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t1: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t2: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t3: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t4: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t6: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t7: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t8: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t9: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t10: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t11: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ks1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ks2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ks3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    n: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    m: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vstmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vstmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[Profile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
