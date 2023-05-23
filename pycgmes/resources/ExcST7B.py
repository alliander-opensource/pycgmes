"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcST7B(ExcitationSystemDynamics):
    """
    Modified IEEE ST7B static excitation system without stator current limiter (SCL) and current compensator (DROOP)
      inputs.

    kh: High-value gate feedback gain (Kh) (>= 0).  Typical value = 1.
    kia: Voltage regulator integral gain (Kia) (>= 0).  Typical value = 1.
    kl: Low-value gate feedback gain (Kl) (>= 0).  Typical value = 1.
    kpa: Voltage regulator proportional gain (Kpa) (> 0).  Typical value = 40.
    oelin: OEL input selector (OELin). Typical value = noOELinput.
    tb: Regulator lag time constant (Tb) (>= 0).  Typical value = 1.
    tc: Regulator lead time constant (Tc) (>= 0).  Typical value = 1.
    tf: Excitation control system stabilizer time constant (Tf) (>= 0).  Typical value = 1.
    tg: Feedback time constant of inner loop field voltage regulator (Tg) (>= 0).  Typical value = 1.
    tia: Feedback time constant (Tia) (>= 0).  Typical value = 3.
    ts: Rectifier firing time constant (Ts) (>= 0).  Typical value = 0.
    uelin: UEL input selector (UELin). Typical value = noUELinput.
    vmax: Maximum voltage reference signal (Vmax) (> 0 and > ExcST7B.vmin)).  Typical value = 1,1.
    vmin: Minimum voltage reference signal (Vmin) (> 0 and < ExcST7B.vmax).  Typical value = 0,9.
    vrmax: Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 5.
    vrmin: Minimum voltage regulator output (Vrmin) (< 0).  Typical value = -4,5.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    kh: float = 0.0  # Type #PU in CIM
    kia: float = 0.0  # Type #PU in CIM
    kl: float = 0.0  # Type #PU in CIM
    kpa: float = 0.0  # Type #PU in CIM
    oelin: Optional[str] = None  # Type M:1..1 in CIM
    tb: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM
    tf: int = 0  # Type #Seconds in CIM
    tg: int = 0  # Type #Seconds in CIM
    tia: int = 0  # Type #Seconds in CIM
    ts: int = 0  # Type #Seconds in CIM
    uelin: Optional[str] = None  # Type M:1..1 in CIM
    vmax: float = 0.0  # Type #PU in CIM
    vmin: float = 0.0  # Type #PU in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExcST7B\n"
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
            "kh": [
                self.profiles.DY.value,
            ],
            "kia": [
                self.profiles.DY.value,
            ],
            "kl": [
                self.profiles.DY.value,
            ],
            "kpa": [
                self.profiles.DY.value,
            ],
            "oelin": [
                self.profiles.DY.value,
            ],
            "tb": [
                self.profiles.DY.value,
            ],
            "tc": [
                self.profiles.DY.value,
            ],
            "tf": [
                self.profiles.DY.value,
            ],
            "tg": [
                self.profiles.DY.value,
            ],
            "tia": [
                self.profiles.DY.value,
            ],
            "ts": [
                self.profiles.DY.value,
            ],
            "uelin": [
                self.profiles.DY.value,
            ],
            "vmax": [
                self.profiles.DY.value,
            ],
            "vmin": [
                self.profiles.DY.value,
            ],
            "vrmax": [
                self.profiles.DY.value,
            ],
            "vrmin": [
                self.profiles.DY.value,
            ],
        }
