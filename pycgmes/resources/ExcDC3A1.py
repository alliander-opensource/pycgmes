"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcDC3A1(ExcitationSystemDynamics):
    """
    Modified old IEEE type 3 excitation system.

    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 300.
    ta: Voltage regulator time constant (Ta) (> 0).  Typical value = 0,01.
    vrmax: Maximum voltage regulator output (Vrmax) (> ExcDC3A1.vrmin).  Typical value = 5.
    vrmin: Minimum voltage regulator output (Vrmin) (< 0 and < ExcDC3A1.vrmax).  Typical value = 0.
    te: Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 1,83.
    kf: Excitation control system stabilizer gain (Kf) (>= 0).  Typical value = 0,1.
    tf: Excitation control system stabilizer time constant (Tf) (>= 0).  Typical value = 0,675.
    kp: Potential circuit gain coefficient (Kp) (>= 0).  Typical value = 4,37.
    ki: Potential circuit gain coefficient (Ki) (>= 0).  Typical value = 4,83.
    vbmax: Available exciter voltage limiter (Vbmax) (> 0).  Typical value = 11,63.
    exclim: (exclim). true = lower limit of zero is applied to integrator output false = lower limit of zero not applied
      to integrator output. Typical value = true.
    ke: Exciter constant related to self-excited field (Ke).  Typical value = 1.
    vb1max: Available exciter voltage limiter (Vb1max) (> 0).  Typical value = 11,63.
    vblim: Vb limiter indicator. true = exciter Vbmax limiter is active false = Vb1max is active.  Typical value = true.
    """

    ka: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    te: int = 0  # Type #Seconds in CIM
    kf: float = 0.0  # Type #PU in CIM
    tf: int = 0  # Type #Seconds in CIM
    kp: float = 0.0  # Type #PU in CIM
    ki: float = 0.0  # Type #PU in CIM
    vbmax: float = 0.0  # Type #PU in CIM
    exclim: bool = False  # Type #Boolean in CIM
    ke: float = 0.0  # Type #PU in CIM
    vb1max: float = 0.0  # Type #PU in CIM
    vblim: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcDC3A1"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "ka": [
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
            "te": [
                Profile.DY.value,
            ],
            "kf": [
                Profile.DY.value,
            ],
            "tf": [
                Profile.DY.value,
            ],
            "kp": [
                Profile.DY.value,
            ],
            "ki": [
                Profile.DY.value,
            ],
            "vbmax": [
                Profile.DY.value,
            ],
            "exclim": [
                Profile.DY.value,
            ],
            "ke": [
                Profile.DY.value,
            ],
            "vb1max": [
                Profile.DY.value,
            ],
            "vblim": [
                Profile.DY.value,
            ],
        }
