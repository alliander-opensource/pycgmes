"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcST3A(ExcitationSystemDynamics):
    """
    Modified IEEE ST3A static excitation system with added speed multiplier.

    vimax: Maximum voltage regulator input limit (Vimax) (> 0).  Typical value = 0,2.
    vimin: Minimum voltage regulator input limit (Vimin) (< 0).  Typical value = -0,2.
    kj: AVR gain (Kj) (> 0).  Typical value = 200.
    tb: Voltage regulator time constant (Tb) (>= 0).  Typical value = 6,67.
    tc: Voltage regulator time constant (Tc) (>= 0).  Typical value = 1.
    efdmax: Maximum AVR output (Efdmax) (>= 0).  Typical value = 6,9.
    km: Forward gain constant of the inner loop field regulator (Km) (> 0).  Typical value = 7,04.
    tm: Forward time constant of inner loop field regulator (Tm) (> 0).  Typical value = 1.
    vrmax: Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 1.
    vrmin: Minimum voltage regulator output (Vrmin) (< 0).  Typical value = -1.
    kg: Feedback gain constant of the inner loop field regulator (Kg) (>= 0).  Typical value = 1.
    kp: Potential source gain (Kp) (> 0).  Typical value = 4,37.
    thetap: Potential circuit phase angle (thetap).  Typical value = 20.
    ki: Potential circuit gain coefficient (Ki) (>= 0).  Typical value = 4,83.
    kc: Rectifier loading factor proportional to commutating reactance (Kc) (>= 0). Typical value = 1,1.
    xl: Reactance associated with potential source (Xl) (>= 0).  Typical value = 0,09.
    vbmax: Maximum excitation voltage (Vbmax) (> 0).  Typical value = 8,63.
    vgmax: Maximum inner loop feedback voltage (Vgmax) (>= 0).  Typical value = 6,53.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical value = 0.
    ks1: Coefficient to allow different usage of the model-speed coefficient (Ks1).  Typical value = 0.
    """

    vimax: float = 0.0  # Type #PU in CIM
    vimin: float = 0.0  # Type #PU in CIM
    kj: float = 0.0  # Type #PU in CIM
    tb: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM
    efdmax: float = 0.0  # Type #PU in CIM
    km: float = 0.0  # Type #PU in CIM
    tm: int = 0  # Type #Seconds in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    kg: float = 0.0  # Type #PU in CIM
    kp: float = 0.0  # Type #PU in CIM
    thetap: float = 0.0  # Type #AngleDegrees in CIM
    ki: float = 0.0  # Type #PU in CIM
    kc: float = 0.0  # Type #PU in CIM
    xl: float = 0.0  # Type #PU in CIM
    vbmax: float = 0.0  # Type #PU in CIM
    vgmax: float = 0.0  # Type #PU in CIM
    ks: float = 0.0  # Type #PU in CIM
    ks1: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcST3A"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "vimax": [
                Profile.DY.value,
            ],
            "vimin": [
                Profile.DY.value,
            ],
            "kj": [
                Profile.DY.value,
            ],
            "tb": [
                Profile.DY.value,
            ],
            "tc": [
                Profile.DY.value,
            ],
            "efdmax": [
                Profile.DY.value,
            ],
            "km": [
                Profile.DY.value,
            ],
            "tm": [
                Profile.DY.value,
            ],
            "vrmax": [
                Profile.DY.value,
            ],
            "vrmin": [
                Profile.DY.value,
            ],
            "kg": [
                Profile.DY.value,
            ],
            "kp": [
                Profile.DY.value,
            ],
            "thetap": [
                Profile.DY.value,
            ],
            "ki": [
                Profile.DY.value,
            ],
            "kc": [
                Profile.DY.value,
            ],
            "xl": [
                Profile.DY.value,
            ],
            "vbmax": [
                Profile.DY.value,
            ],
            "vgmax": [
                Profile.DY.value,
            ],
            "ks": [
                Profile.DY.value,
            ],
            "ks1": [
                Profile.DY.value,
            ],
        }
