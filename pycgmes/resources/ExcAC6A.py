"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcAC6A(ExcitationSystemDynamics):
    """
    Modified IEEE AC6A alternator-supplied rectifier excitation system with speed input.

    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 536.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical value = 0.
    ta: Voltage regulator time constant (Ta) (>= 0).  Typical value = 0,086.
    tk: Voltage regulator time constant (Tk) (>= 0).  Typical value = 0,18.
    tb: Voltage regulator time constant (Tb) (>= 0).  Typical value = 9.
    tc: Voltage regulator time constant (Tc) (>= 0).  Typical value = 3.
    vamax: Maximum voltage regulator output (Vamax) (> 0).  Typical value = 75.
    vamin: Minimum voltage regulator output (Vamin) (< 0).  Typical value = -75.
    vrmax: Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 44.
    vrmin: Minimum voltage regulator output (Vrmin) (< 0).  Typical value = -36.
    te: Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 1.
    kh: Exciter field current limiter gain (Kh) (>= 0).  Typical value = 92.
    tj: Exciter field current limiter time constant (Tj) (>= 0).  Typical value = 0,02.
    th: Exciter field current limiter time constant (Th) (> 0).  Typical value = 0,08.
    vfelim: Exciter field current limit reference (Vfelim) (> 0).  Typical value = 19.
    vhmax: Maximum field current limiter signal reference (Vhmax) (> 0).  Typical value = 75.
    kc: Rectifier loading factor proportional to commutating reactance (Kc) (>= 0).  Typical value = 0,173.
    kd: Demagnetizing factor, a function of exciter alternator reactances (Kd) (>= 0).  Typical value = 1,91.
    ke: Exciter constant related to self-excited field (Ke).  Typical value = 1,6.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1) (> 0).
      Typical value = 7,4.
    seve1: Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance
      (Se[Ve1]) (>= 0).  Typical value = 0,214.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2) (> 0).
      Typical value = 5,55.
    seve2: Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance
      (Se[Ve2]) (>= 0).  Typical value = 0,044.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ka: float = 0.0  # Type #PU in CIM
    ks: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    tk: int = 0  # Type #Seconds in CIM
    tb: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM
    vamax: float = 0.0  # Type #PU in CIM
    vamin: float = 0.0  # Type #PU in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    te: int = 0  # Type #Seconds in CIM
    kh: float = 0.0  # Type #PU in CIM
    tj: int = 0  # Type #Seconds in CIM
    th: int = 0  # Type #Seconds in CIM
    vfelim: float = 0.0  # Type #PU in CIM
    vhmax: float = 0.0  # Type #PU in CIM
    kc: float = 0.0  # Type #PU in CIM
    kd: float = 0.0  # Type #PU in CIM
    ke: float = 0.0  # Type #PU in CIM
    ve1: float = 0.0  # Type #PU in CIM
    seve1: float = 0.0  # Type #Float in CIM
    ve2: float = 0.0  # Type #PU in CIM
    seve2: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExcAC6A\n"
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
            "ks": [
                self.profiles.DY.value,
            ],
            "ta": [
                self.profiles.DY.value,
            ],
            "tk": [
                self.profiles.DY.value,
            ],
            "tb": [
                self.profiles.DY.value,
            ],
            "tc": [
                self.profiles.DY.value,
            ],
            "vamax": [
                self.profiles.DY.value,
            ],
            "vamin": [
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
            "kh": [
                self.profiles.DY.value,
            ],
            "tj": [
                self.profiles.DY.value,
            ],
            "th": [
                self.profiles.DY.value,
            ],
            "vfelim": [
                self.profiles.DY.value,
            ],
            "vhmax": [
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
            "ve1": [
                self.profiles.DY.value,
            ],
            "seve1": [
                self.profiles.DY.value,
            ],
            "ve2": [
                self.profiles.DY.value,
            ],
            "seve2": [
                self.profiles.DY.value,
            ],
        }
