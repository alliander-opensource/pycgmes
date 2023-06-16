"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcIEEEST4B(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type ST4B model. This model is a variation of the type ST3A model, with a proportional plus integral
      (PI) regulator block replacing the lag-lead regulator characteristic that is in the ST3A model. Both potential
      and compound source rectifier excitation systems are modelled.  The PI regulator blocks have non-windup limits
      that are represented. The voltage regulator of this model is typically implemented digitally. Reference: IEEE
      421.5-2005, 7.4.

    kpr: Voltage regulator proportional gain (KPR).  Typical value = 10,75.
    kir: Voltage regulator integral gain (KIR).  Typical value = 10,75.
    ta: Voltage regulator time constant (TA) (>= 0).  Typical value = 0,02.
    vrmax: Maximum voltage regulator output (VRMAX) (> 0).  Typical value = 1.
    vrmin: Minimum voltage regulator output (VRMIN) (< 0).  Typical value = -0,87.
    kpm: Voltage regulator proportional gain output (KPM).  Typical value = 1.
    kim: Voltage regulator integral gain output (KIM).  Typical value = 0.
    vmmax: Maximum inner loop output (VMMax) (> ExcIEEEST4B.vmmin).  Typical value = 99.
    vmmin: Minimum inner loop output (VMMin) (< ExcIEEEST4B.vmmax).  Typical value = -99.
    kg: Feedback gain constant of the inner loop field regulator (KG) (>= 0).  Typical value = 0.
    kp: Potential circuit gain coefficient (KP) (> 0).  Typical value = 9,3.
    thetap: Potential circuit phase angle (thetap).  Typical value = 0.
    ki: Potential circuit gain coefficient (KI) (>= 0).  Typical value = 0.
    kc: Rectifier loading factor proportional to commutating reactance (KC) (>= 0). Typical value = 0,113.
    xl: Reactance associated with potential source (XL) (>= 0).  Typical value = 0,124.
    vbmax: Maximum excitation voltage (VBMax) (> 0).  Typical value = 11,63.
    """

    kpr: float = 0.0  # Type #PU in CIM
    kir: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    kpm: float = 0.0  # Type #PU in CIM
    kim: float = 0.0  # Type #PU in CIM
    vmmax: float = 0.0  # Type #PU in CIM
    vmmin: float = 0.0  # Type #PU in CIM
    kg: float = 0.0  # Type #PU in CIM
    kp: float = 0.0  # Type #PU in CIM
    thetap: float = 0.0  # Type #AngleDegrees in CIM
    ki: float = 0.0  # Type #PU in CIM
    kc: float = 0.0  # Type #PU in CIM
    xl: float = 0.0  # Type #PU in CIM
    vbmax: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcIEEEST4B"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "kpr": [
                Profile.DY.value,
            ],
            "kir": [
                Profile.DY.value,
            ],
            "ta": [
                Profile.DY.value,
            ],
            "vrmax": [
                Profile.DY.value,
            ],
            "vrmin": [
                Profile.DY.value,
            ],
            "kpm": [
                Profile.DY.value,
            ],
            "kim": [
                Profile.DY.value,
            ],
            "vmmax": [
                Profile.DY.value,
            ],
            "vmmin": [
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
        }
