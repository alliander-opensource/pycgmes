"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcIEEEAC7B(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type AC7B model. The model represents excitation systems which consist of an AC alternator with
      either stationary or rotating rectifiers to produce the DC field requirements. It is an upgrade to earlier AC
      excitation systems, which replace only the controls but retain the AC alternator and diode rectifier bridge.
      Reference: IEEE 421.5-2005, 6.7. Note, however, that in IEEE 421.5-2005, the [1 / sTE] block is shown as [1 /
      (1 + sTE)], which is incorrect.

    kpr: Voltage regulator proportional gain (KPR) (> 0 if ExcIEEEAC7B.kir = 0).  Typical value = 4,24.
    kir: Voltage regulator integral gain (KIR) (>= 0).  Typical value = 4,24.
    kdr: Voltage regulator derivative gain (KDR) (>= 0).  Typical value = 0.
    tdr: Lag time constant (TDR) (>= 0).  Typical value = 0.
    vrmax: Maximum voltage regulator output (VRMAX) (> 0).  Typical value = 5,79.
    vrmin: Minimum voltage regulator output (VRMIN) (< 0).  Typical value = -5,79.
    kpa: Voltage regulator proportional gain (KPA) (> 0 if ExcIEEEAC7B.kia = 0).  Typical value = 65,36.
    kia: Voltage regulator integral gain (KIA) (>= 0).  Typical value = 59,69.
    vamax: Maximum voltage regulator output (VAMAX) (> 0).  Typical value = 1.
    vamin: Minimum voltage regulator output (VAMIN) (< 0).  Typical value = -0,95.
    kp: Potential circuit gain coefficient (KP) (> 0).  Typical value = 4,96.
    kl: Exciter field voltage lower limit parameter (KL).  Typical value = 10.
    te: Exciter time constant, integration rate associated with exciter control (TE) (> 0).  Typical value = 1,1.
    vfemax: Exciter field current limit reference (VFEMAX).  Typical value = 6,9.
    vemin: Minimum exciter voltage output (VEMIN) (<= 0).  Typical value = 0.
    ke: Exciter constant related to self-excited field (KE).  Typical value = 1.
    kc: Rectifier loading factor proportional to commutating reactance (KC) (>= 0). Typical value = 0,18.
    kd: Demagnetizing factor, a function of exciter alternator reactances (KD) (>= 0).  Typical value = 0,02.
    kf1: Excitation control system stabilizer gain (KF1) (>= 0).  Typical value = 0,212.
    kf2: Excitation control system stabilizer gain (KF2) (>= 0).  Typical value = 0.
    kf3: Excitation control system stabilizer gain (KF3) (>= 0).  Typical value = 0.
    tf: Excitation control system stabilizer time constant (TF) (> 0).  Typical value = 1.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (VE1) (> 0).
      Typical value = 6,3.
    seve1: Exciter saturation function value at the corresponding exciter voltage, VE1, back of commutating reactance
      (SE[VE1]) (>= 0).  Typical value = 0,44.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (VE2) (> 0).
      Typical value = 3,02.
    seve2: Exciter saturation function value at the corresponding exciter voltage, VE2, back of commutating reactance
      (SE[VE2]) (>= 0).  Typical value = 0,075.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    kpr: float = 0.0  # Type #PU in CIM
    kir: float = 0.0  # Type #PU in CIM
    kdr: float = 0.0  # Type #PU in CIM
    tdr: int = 0  # Type #Seconds in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    kpa: float = 0.0  # Type #PU in CIM
    kia: float = 0.0  # Type #PU in CIM
    vamax: float = 0.0  # Type #PU in CIM
    vamin: float = 0.0  # Type #PU in CIM
    kp: float = 0.0  # Type #PU in CIM
    kl: float = 0.0  # Type #PU in CIM
    te: int = 0  # Type #Seconds in CIM
    vfemax: float = 0.0  # Type #PU in CIM
    vemin: float = 0.0  # Type #PU in CIM
    ke: float = 0.0  # Type #PU in CIM
    kc: float = 0.0  # Type #PU in CIM
    kd: float = 0.0  # Type #PU in CIM
    kf1: float = 0.0  # Type #PU in CIM
    kf2: float = 0.0  # Type #PU in CIM
    kf3: float = 0.0  # Type #PU in CIM
    tf: int = 0  # Type #Seconds in CIM
    ve1: float = 0.0  # Type #PU in CIM
    seve1: float = 0.0  # Type #Float in CIM
    ve2: float = 0.0  # Type #PU in CIM
    seve2: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExcIEEEAC7B\n"
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
            "kpr": [
                self.profiles.DY.value,
            ],
            "kir": [
                self.profiles.DY.value,
            ],
            "kdr": [
                self.profiles.DY.value,
            ],
            "tdr": [
                self.profiles.DY.value,
            ],
            "vrmax": [
                self.profiles.DY.value,
            ],
            "vrmin": [
                self.profiles.DY.value,
            ],
            "kpa": [
                self.profiles.DY.value,
            ],
            "kia": [
                self.profiles.DY.value,
            ],
            "vamax": [
                self.profiles.DY.value,
            ],
            "vamin": [
                self.profiles.DY.value,
            ],
            "kp": [
                self.profiles.DY.value,
            ],
            "kl": [
                self.profiles.DY.value,
            ],
            "te": [
                self.profiles.DY.value,
            ],
            "vfemax": [
                self.profiles.DY.value,
            ],
            "vemin": [
                self.profiles.DY.value,
            ],
            "ke": [
                self.profiles.DY.value,
            ],
            "kc": [
                self.profiles.DY.value,
            ],
            "kd": [
                self.profiles.DY.value,
            ],
            "kf1": [
                self.profiles.DY.value,
            ],
            "kf2": [
                self.profiles.DY.value,
            ],
            "kf3": [
                self.profiles.DY.value,
            ],
            "tf": [
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
