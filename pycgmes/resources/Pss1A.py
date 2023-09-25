"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

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

    inputSignalType: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    a1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    a2: float = Field(
        default=0.0,
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

    t5: int = Field(
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

    ks: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vrmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vrmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vcu: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vcl: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    a3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    a4: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    a5: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    a6: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    a7: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    a8: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kd: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    tdelay: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
