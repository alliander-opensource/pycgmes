"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcAC1A(ExcitationSystemDynamics):
    """
    Modified IEEE AC1A alternator-supplied rectifier excitation system with different rate feedback source.

    tb: Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.
    tc: Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.
    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 400.
    ta: Voltage regulator time constant (Ta) (> 0).  Typical value = 0,02.
    vamax: Maximum voltage regulator output (Vamax) (> 0).  Typical value = 14,5.
    vamin: Minimum voltage regulator output (Vamin) (< 0).  Typical value = -14,5.
    te: Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 0,8.
    kf: Excitation control system stabilizer gains (Kf) (>= 0).  Typical value = 0,03.
    kf1: Coefficient to allow different usage of the model (Kf1) (>= 0).  Typical value = 0.
    kf2: Coefficient to allow different usage of the model (Kf2) (>= 0).  Typical value = 1.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks) (>= 0).  Typical value = 0.
    tf: Excitation control system stabilizer time constant (Tf) (> 0).  Typical value = 1.
    kc: Rectifier loading factor proportional to commutating reactance (Kc) (>= 0). Typical value = 0,2.
    kd: Demagnetizing factor, a function of exciter alternator reactances (Kd) (>= 0).  Typical value = 0,38.
    ke: Exciter constant related to self-excited field (Ke).  Typical value = 1.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1) (> 0).
      Typical value = 4,18.
    seve1: Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance
      (Se[Ve1]) (>= 0).  Typical value = 0,1.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2) (> 0).
      Typical value = 3,14.
    seve2: Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance
      (Se[Ve2]) (>= 0).  Typical value = 0,03.
    vrmax: Maximum voltage regulator outputs (Vrmax) (> 0).  Typical value = 6,03.
    vrmin: Minimum voltage regulator outputs (Vrmin) (< 0).  Typical value = -5,43.
    hvlvgates: Indicates if both HV gate and LV gate are active (HVLVgates). true = gates are used false = gates are not
      used. Typical value = true.
    """

    tb: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM
    ka: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    vamax: float = 0.0  # Type #PU in CIM
    vamin: float = 0.0  # Type #PU in CIM
    te: int = 0  # Type #Seconds in CIM
    kf: float = 0.0  # Type #PU in CIM
    kf1: float = 0.0  # Type #PU in CIM
    kf2: float = 0.0  # Type #PU in CIM
    ks: float = 0.0  # Type #PU in CIM
    tf: int = 0  # Type #Seconds in CIM
    kc: float = 0.0  # Type #PU in CIM
    kd: float = 0.0  # Type #PU in CIM
    ke: float = 0.0  # Type #PU in CIM
    ve1: float = 0.0  # Type #PU in CIM
    seve1: float = 0.0  # Type #Float in CIM
    ve2: float = 0.0  # Type #PU in CIM
    seve2: float = 0.0  # Type #Float in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    hvlvgates: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcAC1A"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "kf": [
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
            "vrmax": [
                Profile.DY.value,
            ],
            "vrmin": [
                Profile.DY.value,
            ],
            "hvlvgates": [
                Profile.DY.value,
            ],
        }
