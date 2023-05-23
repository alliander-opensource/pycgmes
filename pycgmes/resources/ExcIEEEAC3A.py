"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcIEEEAC3A(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type AC3A model. The model represents the field-controlled alternator-rectifier excitation systems
      designated type AC3A. These excitation systems include an alternator main exciter with non-controlled
      rectifiers. The exciter employs self-excitation, and the voltage regulator power is derived from the exciter
      output voltage.  Therefore, this system has an additional nonlinearity, simulated by the use of a multiplier
      whose inputs are the voltage regulator command signal, Va, and the exciter output voltage, Efd, times KR.
      This model is applicable to excitation systems employing static voltage regulators. Reference: IEEE
      421.5-2005, 6.3.

    tb: Voltage regulator time constant (TB) (>= 0).  Typical value = 0.
    tc: Voltage regulator time constant (TC) (>= 0).  Typical value = 0.
    ka: Voltage regulator gain (KA) (> 0).  Typical value = 45,62.
    ta: Voltage regulator time constant (TA) (> 0).  Typical value = 0,013.
    vamax: Maximum voltage regulator output (VAMAX) (> 0).  Typical value = 1.
    vamin: Minimum voltage regulator output (VAMIN) (< 0).  Typical value = -0,95.
    te: Exciter time constant, integration rate associated with exciter control (TE) (> 0).  Typical value = 1,17.
    vemin: Minimum exciter voltage output (VEMIN) (<= 0).  Typical value = 0.
    kr: Constant associated with regulator and alternator field power supply (KR) (> 0).  Typical value = 3,77.
    kf: Excitation control system stabilizer gains (KF) (>= 0).  Typical value = 0,143.
    tf: Excitation control system stabilizer time constant (TF) (> 0).  Typical value = 1.
    kn: Excitation control system stabilizer gain (KN) (>= 0).  Typical value = 0,05.
    efdn: Value of Efd at which feedback gain changes (EFDN) (> 0).  Typical value = 2,36.
    kc: Rectifier loading factor proportional to commutating reactance (KC) (>= 0).  Typical value = 0,104.
    kd: Demagnetizing factor, a function of exciter alternator reactances (KD) (>= 0).  Typical value = 0,499.
    ke: Exciter constant related to self-excited field (KE).  Typical value = 1.
    vfemax: Exciter field current limit reference (VFEMAX) (>= 0).  Typical value = 16.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (VE1) (> 0).
      Typical value = 6,24.
    seve1: Exciter saturation function value at the corresponding exciter voltage, VE1, back of commutating reactance
      (SE[VE1]) (>= 0).  Typical value = 1,143.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (VE2) (> 0).
      Typical value = 4,68.
    seve2: Exciter saturation function value at the corresponding exciter voltage, VE2, back of commutating reactance
      (SE[VE2]) (>= 0).  Typical value = 0,1.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    tb: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM
    ka: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    vamax: float = 0.0  # Type #PU in CIM
    vamin: float = 0.0  # Type #PU in CIM
    te: int = 0  # Type #Seconds in CIM
    vemin: float = 0.0  # Type #PU in CIM
    kr: float = 0.0  # Type #PU in CIM
    kf: float = 0.0  # Type #PU in CIM
    tf: int = 0  # Type #Seconds in CIM
    kn: float = 0.0  # Type #PU in CIM
    efdn: float = 0.0  # Type #PU in CIM
    kc: float = 0.0  # Type #PU in CIM
    kd: float = 0.0  # Type #PU in CIM
    ke: float = 0.0  # Type #PU in CIM
    vfemax: float = 0.0  # Type #PU in CIM
    ve1: float = 0.0  # Type #PU in CIM
    seve1: float = 0.0  # Type #Float in CIM
    ve2: float = 0.0  # Type #PU in CIM
    seve2: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExcIEEEAC3A\n"
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
            "tb": [
                self.profiles.DY.value,
            ],
            "tc": [
                self.profiles.DY.value,
            ],
            "ka": [
                self.profiles.DY.value,
            ],
            "ta": [
                self.profiles.DY.value,
            ],
            "vamax": [
                self.profiles.DY.value,
            ],
            "vamin": [
                self.profiles.DY.value,
            ],
            "te": [
                self.profiles.DY.value,
            ],
            "vemin": [
                self.profiles.DY.value,
            ],
            "kr": [
                self.profiles.DY.value,
            ],
            "kf": [
                self.profiles.DY.value,
            ],
            "tf": [
                self.profiles.DY.value,
            ],
            "kn": [
                self.profiles.DY.value,
            ],
            "efdn": [
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
            "vfemax": [
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
