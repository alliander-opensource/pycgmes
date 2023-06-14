"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcAC2A(ExcitationSystemDynamics):
    """
    Modified IEEE AC2A alternator-supplied rectifier excitation system with different field current limit.

    tb: Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.
    tc: Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.
    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 400.
    ta: Voltage regulator time constant (Ta) (> 0).  Typical value = 0,02.
    vamax: Maximum voltage regulator output (Vamax) (> 0).  Typical value = 8.
    vamin: Minimum voltage regulator output (Vamin) (< 0).  Typical value = -8.
    kb: Second stage regulator gain (Kb) (> 0).  Exciter field current controller gain.  Typical value = 25.
    kb1: Second stage regulator gain (Kb1). It is exciter field current controller gain used as alternative to Kb to
      represent a variant of the ExcAC2A model.  Typical value = 25.
    vrmax: Maximum voltage regulator outputs (Vrmax) (> 0).  Typical value = 105.
    vrmin: Minimum voltage regulator outputs (Vrmin) (< 0).  Typical value = -95.
    te: Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 0,6.
    vfemax: Exciter field current limit reference (Vfemax) (>= 0).  Typical value = 4,4.
    kh: Exciter field current feedback gain (Kh) (>= 0).  Typical value = 1.
    kf: Excitation control system stabilizer gains (Kf) (>= 0).  Typical value = 0,03.
    kl: Exciter field current limiter gain (Kl).  Typical value = 10.
    vlr: Maximum exciter field current (Vlr) (> 0).  Typical value = 4,4.
    kl1: Coefficient to allow different usage of the model (Kl1).  Typical value = 1.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks) (>= 0).  Typical value = 0.
    tf: Excitation control system stabilizer time constant (Tf) (> 0).  Typical value = 1.
    kc: Rectifier loading factor proportional to commutating reactance (Kc) (>= 0).  Typical value = 0,28.
    kd: Demagnetizing factor, a function of exciter alternator reactances (Kd) (>= 0).  Typical value = 0,35.
    ke: Exciter constant related to self-excited field (Ke).  Typical value = 1.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1) (> 0).
      Typical value = 4,4.
    seve1: Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance
      (Se[Ve1]) (>= 0).  Typical value = 0,037.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2) (> 0).
      Typical value = 3,3.
    seve2: Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance
      (Se[Ve2]) (>= 0).  Typical value = 0,012.
    hvgate: Indicates if HV gate is active (HVgate). true = gate is used false = gate is not used. Typical value = true.
    lvgate: Indicates if LV gate is active (LVgate). true = gate is used false = gate is not used. Typical value = true.
    """

    tb: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM
    ka: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    vamax: float = 0.0  # Type #PU in CIM
    vamin: float = 0.0  # Type #PU in CIM
    kb: float = 0.0  # Type #PU in CIM
    kb1: float = 0.0  # Type #PU in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    te: int = 0  # Type #Seconds in CIM
    vfemax: float = 0.0  # Type #PU in CIM
    kh: float = 0.0  # Type #PU in CIM
    kf: float = 0.0  # Type #PU in CIM
    kl: float = 0.0  # Type #PU in CIM
    vlr: float = 0.0  # Type #PU in CIM
    kl1: float = 0.0  # Type #PU in CIM
    ks: float = 0.0  # Type #PU in CIM
    tf: int = 0  # Type #Seconds in CIM
    kc: float = 0.0  # Type #PU in CIM
    kd: float = 0.0  # Type #PU in CIM
    ke: float = 0.0  # Type #PU in CIM
    ve1: float = 0.0  # Type #PU in CIM
    seve1: float = 0.0  # Type #Float in CIM
    ve2: float = 0.0  # Type #PU in CIM
    seve2: float = 0.0  # Type #Float in CIM
    hvgate: bool = False  # Type #Boolean in CIM
    lvgate: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcAC2A"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "kb": [
                Profile.DY.value,
            ],
            "kb1": [
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
            "vfemax": [
                Profile.DY.value,
            ],
            "kh": [
                Profile.DY.value,
            ],
            "kf": [
                Profile.DY.value,
            ],
            "kl": [
                Profile.DY.value,
            ],
            "vlr": [
                Profile.DY.value,
            ],
            "kl1": [
                Profile.DY.value,
            ],
            "ks": [
                Profile.DY.value,
            ],
            "tf": [
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
            "hvgate": [
                Profile.DY.value,
            ],
            "lvgate": [
                Profile.DY.value,
            ],
        }
