"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcREXS(ExcitationSystemDynamics):
    """
    General purpose rotating excitation system.  This model can be used to represent a wide range of excitation systems
      whose DC power source is an AC or DC generator. It encompasses IEEE type AC1, AC2, DC1, and DC2 excitation
      system models.

    e1: Field voltage value 1 (E1).  Typical value = 3.
    e2: Field voltage value 2 (E2).  Typical value = 4.
    fbf: Rate feedback signal flag (fbf). Typical value = fieldCurrent.
    flimf: Limit type flag (Flimf).  Typical value = 0.
    kc: Rectifier regulation factor (Kc).  Typical value = 0,05.
    kd: Exciter regulation factor (Kd).  Typical value = 2.
    ke: Exciter field proportional constant (Ke).  Typical value = 1.
    kefd: Field voltage feedback gain (Kefd).  Typical value = 0.
    kf: Rate feedback gain (Kf) (>= 0).  Typical value = 0,05.
    kh: Field voltage controller feedback gain (Kh).  Typical value = 0.
    kii: Field current regulator integral gain (Kii).  Typical value = 0.
    kip: Field current regulator proportional gain (Kip).  Typical value = 1.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical value = 0.
    kvi: Voltage regulator integral gain (Kvi).  Typical value = 0.
    kvp: Voltage regulator proportional gain (Kvp).  Typical value = 2800.
    kvphz: V/Hz limiter gain (Kvphz).  Typical value = 0.
    nvphz: Pickup speed of V/Hz limiter (Nvphz).  Typical value = 0.
    se1: Saturation factor at E1 (Se1).  Typical value = 0,0001.
    se2: Saturation factor at E2 (Se2).  Typical value = 0,001.
    ta: Voltage regulator time constant (Ta) (>= 0).  If = 0, block is bypassed.  Typical value = 0,01.
    tb1: Lag time constant (Tb1) (>= 0).  If = 0, block is bypassed.  Typical value = 0.
    tb2: Lag time constant (Tb2) (>= 0).  If = 0, block is bypassed.  Typical value = 0.
    tc1: Lead time constant (Tc1) (>= 0).  Typical value = 0.
    tc2: Lead time constant (Tc2) (>= 0).  Typical value = 0.
    te: Exciter field time constant (Te) (> 0).  Typical value = 1,2.
    tf: Rate feedback time constant (Tf) (>= 0).  If = 0, the feedback path is not used.  Typical value = 1.
    tf1: Feedback lead time constant (Tf1) (>= 0).  Typical value = 0.
    tf2: Feedback lag time constant (Tf2) (>= 0).  If = 0, block is bypassed.  Typical value = 0.
    tp: Field current bridge time constant (Tp) (>= 0).  Typical value = 0.
    vcmax: Maximum compounding voltage (Vcmax).  Typical value = 0.
    vfmax: Maximum exciter field current (Vfmax) (> ExcREXS.vfmin).  Typical value = 47.
    vfmin: Minimum exciter field current (Vfmin) (< ExcREXS.vfmax).  Typical value = -20.
    vimax: Voltage regulator input limit (Vimax).  Typical value = 0,1.
    vrmax: Maximum controller output (Vrmax) (> ExcREXS.vrmin).  Typical value = 47.
    vrmin: Minimum controller output (Vrmin) (< ExcREXS.vrmax).  Typical value = -20.
    xc: Exciter compounding reactance (Xc).  Typical value = 0.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    e1: float = 0.0  # Type #PU in CIM
    e2: float = 0.0  # Type #PU in CIM
    fbf: Optional[str] = None  # Type M:1..1 in CIM
    flimf: float = 0.0  # Type #PU in CIM
    kc: float = 0.0  # Type #PU in CIM
    kd: float = 0.0  # Type #PU in CIM
    ke: float = 0.0  # Type #PU in CIM
    kefd: float = 0.0  # Type #PU in CIM
    kf: int = 0  # Type #Seconds in CIM
    kh: float = 0.0  # Type #PU in CIM
    kii: float = 0.0  # Type #PU in CIM
    kip: float = 0.0  # Type #PU in CIM
    ks: float = 0.0  # Type #PU in CIM
    kvi: float = 0.0  # Type #PU in CIM
    kvp: float = 0.0  # Type #PU in CIM
    kvphz: float = 0.0  # Type #PU in CIM
    nvphz: float = 0.0  # Type #PU in CIM
    se1: float = 0.0  # Type #PU in CIM
    se2: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    tb1: int = 0  # Type #Seconds in CIM
    tb2: int = 0  # Type #Seconds in CIM
    tc1: int = 0  # Type #Seconds in CIM
    tc2: int = 0  # Type #Seconds in CIM
    te: int = 0  # Type #Seconds in CIM
    tf: int = 0  # Type #Seconds in CIM
    tf1: int = 0  # Type #Seconds in CIM
    tf2: int = 0  # Type #Seconds in CIM
    tp: int = 0  # Type #Seconds in CIM
    vcmax: float = 0.0  # Type #PU in CIM
    vfmax: float = 0.0  # Type #PU in CIM
    vfmin: float = 0.0  # Type #PU in CIM
    vimax: float = 0.0  # Type #PU in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    xc: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExcREXS\n"
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
            "e1": [
                self.profiles.DY.value,
            ],
            "e2": [
                self.profiles.DY.value,
            ],
            "fbf": [
                self.profiles.DY.value,
            ],
            "flimf": [
                self.profiles.DY.value,
            ],
            "kc": [
                self.profiles.DY.value,
            ],
            "kd": [
                self.profiles.DY.value,
            ],
            "ke": [
                self.profiles.DY.value,
            ],
            "kefd": [
                self.profiles.DY.value,
            ],
            "kf": [
                self.profiles.DY.value,
            ],
            "kh": [
                self.profiles.DY.value,
            ],
            "kii": [
                self.profiles.DY.value,
            ],
            "kip": [
                self.profiles.DY.value,
            ],
            "ks": [
                self.profiles.DY.value,
            ],
            "kvi": [
                self.profiles.DY.value,
            ],
            "kvp": [
                self.profiles.DY.value,
            ],
            "kvphz": [
                self.profiles.DY.value,
            ],
            "nvphz": [
                self.profiles.DY.value,
            ],
            "se1": [
                self.profiles.DY.value,
            ],
            "se2": [
                self.profiles.DY.value,
            ],
            "ta": [
                self.profiles.DY.value,
            ],
            "tb1": [
                self.profiles.DY.value,
            ],
            "tb2": [
                self.profiles.DY.value,
            ],
            "tc1": [
                self.profiles.DY.value,
            ],
            "tc2": [
                self.profiles.DY.value,
            ],
            "te": [
                self.profiles.DY.value,
            ],
            "tf": [
                self.profiles.DY.value,
            ],
            "tf1": [
                self.profiles.DY.value,
            ],
            "tf2": [
                self.profiles.DY.value,
            ],
            "tp": [
                self.profiles.DY.value,
            ],
            "vcmax": [
                self.profiles.DY.value,
            ],
            "vfmax": [
                self.profiles.DY.value,
            ],
            "vfmin": [
                self.profiles.DY.value,
            ],
            "vimax": [
                self.profiles.DY.value,
            ],
            "vrmax": [
                self.profiles.DY.value,
            ],
            "vrmin": [
                self.profiles.DY.value,
            ],
            "xc": [
                self.profiles.DY.value,
            ],
        }
