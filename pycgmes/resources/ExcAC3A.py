"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcAC3A(ExcitationSystemDynamics):
    """
    Modified IEEE AC3A alternator-supplied rectifier excitation system with different field current limit.

    tb: Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.
    tc: Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.
    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 45,62.
    ta: Voltage regulator time constant (Ta) (> 0).  Typical value = 0,013.
    vamax: Maximum voltage regulator output (Vamax) (> 0).  Typical value = 1.
    vamin: Minimum voltage regulator output (Vamin) (< 0).  Typical value = -0,95.
    te: Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 1,17.
    vemin: Minimum exciter voltage output (Vemin) (<= 0).  Typical value = 0.
    kr: Constant associated with regulator and alternator field power supply (Kr) (> 0).  Typical value =3,77.
    kf: Excitation control system stabilizer gains (Kf) (>= 0).  Typical value = 0,143.
    tf: Excitation control system stabilizer time constant (Tf) (> 0).  Typical value = 1.
    kn: Excitation control system stabilizer gain (Kn) (>= 0).  Typical value =0,05.
    efdn: Value of Efd at which feedback gain changes (Efdn) (> 0).  Typical value = 2,36.
    kc: Rectifier loading factor proportional to commutating reactance (Kc) (>= 0).  Typical value = 0,104.
    kd: Demagnetizing factor, a function of exciter alternator reactances (Kd) (>= 0).  Typical value = 0,499.
    ke: Exciter constant related to self-excited field (Ke).  Typical value = 1.
    klv: Gain used in the minimum field voltage limiter loop (Klv).  Typical value = 0,194.
    kf1: Coefficient to allow different usage of the model (Kf1).  Typical value = 1.
    kf2: Coefficient to allow different usage of the model (Kf2).  Typical value = 0.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical value = 0.
    vfemax: Exciter field current limit reference (Vfemax) (>= 0).  Typical value = 16.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1) (> 0).
      Typical value = 6.24.
    seve1: Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance
      (Se[Ve1]) (>= 0).  Typical value = 1,143.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2) (> 0).
      Typical value = 4,68.
    seve2: Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance
      (Se[Ve2]) (>= 0).  Typical value = 0,1.
    vlv: Field voltage used in the minimum field voltage limiter loop (Vlv).  Typical value = 0,79.
    """

    tb: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM
    ka: int = 0  # Type #Seconds in CIM
    ta: float = 0.0  # Type #PU in CIM
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
    klv: float = 0.0  # Type #PU in CIM
    kf1: float = 0.0  # Type #PU in CIM
    kf2: float = 0.0  # Type #PU in CIM
    ks: float = 0.0  # Type #PU in CIM
    vfemax: float = 0.0  # Type #PU in CIM
    ve1: float = 0.0  # Type #PU in CIM
    seve1: float = 0.0  # Type #Float in CIM
    ve2: float = 0.0  # Type #PU in CIM
    seve2: float = 0.0  # Type #Float in CIM
    vlv: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcAC3A"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "tb": [
                Profile.DY.value,
            ],
            "tc": [
                Profile.DY.value,
            ],
            "ka": [
                Profile.DY.value,
            ],
            "ta": [
                Profile.DY.value,
            ],
            "vamax": [
                Profile.DY.value,
            ],
            "vamin": [
                Profile.DY.value,
            ],
            "te": [
                Profile.DY.value,
            ],
            "vemin": [
                Profile.DY.value,
            ],
            "kr": [
                Profile.DY.value,
            ],
            "kf": [
                Profile.DY.value,
            ],
            "tf": [
                Profile.DY.value,
            ],
            "kn": [
                Profile.DY.value,
            ],
            "efdn": [
                Profile.DY.value,
            ],
            "kc": [
                Profile.DY.value,
            ],
            "kd": [
                Profile.DY.value,
            ],
            "ke": [
                Profile.DY.value,
            ],
            "klv": [
                Profile.DY.value,
            ],
            "kf1": [
                Profile.DY.value,
            ],
            "kf2": [
                Profile.DY.value,
            ],
            "ks": [
                Profile.DY.value,
            ],
            "vfemax": [
                Profile.DY.value,
            ],
            "ve1": [
                Profile.DY.value,
            ],
            "seve1": [
                Profile.DY.value,
            ],
            "ve2": [
                Profile.DY.value,
            ],
            "seve2": [
                Profile.DY.value,
            ],
            "vlv": [
                Profile.DY.value,
            ],
        }
