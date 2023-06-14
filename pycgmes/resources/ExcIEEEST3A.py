"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcIEEEST3A(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type ST3A model.  Some static systems utilize a field voltage control loop to linearize the exciter
      control characteristic. This also makes the output independent of supply source variations until supply
      limitations are reached.  These systems utilize a variety of controlled-rectifier designs: full thyristor
      complements or hybrid bridges in either series or shunt configurations. The power source can consist of only a
      potential source, either fed from the machine terminals or from internal windings. Some designs can have
      compound power sources utilizing both machine potential and current. These power sources are represented as
      phasor combinations of machine terminal current and voltage and are accommodated by suitable parameters in
      model type ST3A which is represented by ExcIEEEST3A. Reference: IEEE 421.5-2005, 7.3.

    vimax: Maximum voltage regulator input limit (VIMAX) (> 0).  Typical value = 0,2.
    vimin: Minimum voltage regulator input limit (VIMIN) (< 0).  Typical value = -0,2.
    ka: Voltage regulator gain (KA) (> 0). This is parameter K in the IEEE standard. Typical value = 200.
    ta: Voltage regulator time constant (TA) (>= 0).  Typical value = 0.
    tb: Voltage regulator time constant (TB) (>= 0).  Typical value = 10.
    tc: Voltage regulator time constant (TC) (>= 0).  Typical value = 1.
    vrmax: Maximum voltage regulator output (VRMAX) (> 0).  Typical value = 10.
    vrmin: Minimum voltage regulator output (VRMIN) (< 0).  Typical value = -10.
    km: Forward gain constant of the inner loop field regulator (KM) (> 0).  Typical value = 7,93.
    tm: Forward time constant of inner loop field regulator (TM) (> 0).  Typical value = 0,4.
    vmmax: Maximum inner loop output (VMMax) (> 0).  Typical value = 1.
    vmmin: Minimum inner loop output (VMMin) (<= 0).  Typical value = 0.
    kg: Feedback gain constant of the inner loop field regulator (KG) (>= 0).  Typical value = 1.
    kp: Potential circuit gain coefficient (KP) (> 0).  Typical value = 6,15.
    thetap: Potential circuit phase angle (thetap).  Typical value = 0.
    ki: Potential circuit gain coefficient (KI) (>= 0).  Typical value = 0.
    kc: Rectifier loading factor proportional to commutating reactance (KC) (>= 0). Typical value = 0,2.
    xl: Reactance associated with potential source (XL) (>= 0).  Typical value = 0,081.
    vbmax: Maximum excitation voltage (VBMax) (> 0).  Typical value = 6,9.
    vgmax: Maximum inner loop feedback voltage (VGMax) (>= 0).  Typical value = 5,8.
    """

    vimax: float = 0.0  # Type #PU in CIM
    vimin: float = 0.0  # Type #PU in CIM
    ka: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    tb: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    km: float = 0.0  # Type #PU in CIM
    tm: int = 0  # Type #Seconds in CIM
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

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcIEEEST3A"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "ka": [
                Profile.DY.value,
            ],
            "ta": [
                Profile.DY.value,
            ],
            "tb": [
                Profile.DY.value,
            ],
            "tc": [
                Profile.DY.value,
            ],
            "vrmax": [
                Profile.DY.value,
            ],
            "vrmin": [
                Profile.DY.value,
            ],
            "km": [
                Profile.DY.value,
            ],
            "tm": [
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
        }
