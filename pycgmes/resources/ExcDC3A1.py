"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=ExcDC3A1\n"
        attributes = self.__dict__
        for key, val in attributes.items():
            str_ = str_ + key + f"={val}\n"
        return str_

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                self.profiles.DY.value,
            ],
            # Attributes
            "ka": [
                self.profiles.DY.value,
            ],
            "ta": [
                self.profiles.DY.value,
            ],
            "vrmax": [
                self.profiles.DY.value,
            ],
            "vrmin": [
                self.profiles.DY.value,
            ],
            "te": [
                self.profiles.DY.value,
            ],
            "kf": [
                self.profiles.DY.value,
            ],
            "tf": [
                self.profiles.DY.value,
            ],
            "kp": [
                self.profiles.DY.value,
            ],
            "ki": [
                self.profiles.DY.value,
            ],
            "vbmax": [
                self.profiles.DY.value,
            ],
            "exclim": [
                self.profiles.DY.value,
            ],
            "ke": [
                self.profiles.DY.value,
            ],
            "vb1max": [
                self.profiles.DY.value,
            ],
            "vblim": [
                self.profiles.DY.value,
            ],
        }
