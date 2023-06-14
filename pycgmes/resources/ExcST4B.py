"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcST4B(ExcitationSystemDynamics):
    """
    Modified IEEE ST4B static excitation system with maximum inner loop feedback gain Vgmax.

    kpr: Voltage regulator proportional gain (Kpr).  Typical value = 10,75.
    kir: Voltage regulator integral gain (Kir).  Typical value = 10,75.
    ta: Voltage regulator time constant (Ta) (>= 0).  Typical value = 0,02.
    vrmax: Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 1.
    vrmin: Minimum voltage regulator output (Vrmin) (< 0).  Typical value = -0,87.
    kpm: Voltage regulator proportional gain output (Kpm).  Typical value = 1.
    kim: Voltage regulator integral gain output (Kim).  Typical value = 0.
    vmmax: Maximum inner loop output (Vmmax) (> ExcST4B.vmmin).  Typical value = 99.
    vmmin: Minimum inner loop output (Vmmin) (< ExcST4B.vmmax).  Typical value = -99.
    kg: Feedback gain constant of the inner loop field regulator (Kg) (>= 0). Typical value = 0.
    kp: Potential circuit gain coefficient (Kp) (> 0).  Typical value = 9,3.
    thetap: Potential circuit phase angle (thetap).  Typical value = 0.
    ki: Potential circuit gain coefficient (Ki) (>= 0).  Typical value = 0.
    kc: Rectifier loading factor proportional to commutating reactance (Kc) (>= 0). Typical value = 0,113.
    xl: Reactance associated with potential source (Xl) (>= 0).  Typical value = 0,124.
    vbmax: Maximum excitation voltage (Vbmax) (> 0).  Typical value = 11,63.
    vgmax: Maximum inner loop feedback voltage (Vgmax) (>= 0).  Typical value = 5,8.
    uel: Selector (UEL). true = UEL is part of block diagram false = UEL is not part of block diagram.  Typical value =
      false.
    lvgate: Selector (LVGate). true = LVGate is part of the block diagram false = LVGate is not part of the block
      diagram.  Typical value = false.
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
    vgmax: float = 0.0  # Type #PU in CIM
    uel: bool = False  # Type #Boolean in CIM
    lvgate: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcST4B"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "vgmax": [
                Profile.DY.value,
            ],
            "uel": [
                Profile.DY.value,
            ],
            "lvgate": [
                Profile.DY.value,
            ],
        }
