"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcIEEEAC2A(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type AC2A model. The model represents a high initial response field-controlled alternator-rectifier
      excitation system. The alternator main exciter is used with non-controlled rectifiers. The type AC2A model is
      similar to that of type AC1A except for the inclusion of exciter time constant compensation and exciter field
      current limiting elements. Reference: IEEE 421.5-2005, 6.2.

    tb: Voltage regulator time constant (TB) (>= 0).  Typical value = 0.
    tc: Voltage regulator time constant (TC) (>= 0).  Typical value = 0.
    ka: Voltage regulator gain (KA) (> 0).  Typical value = 400.
    ta: Voltage regulator time constant (TA) (> 0).  Typical value = 0,02.
    vamax: Maximum voltage regulator output (VAMAX) (> 0).  Typical value = 8.
    vamin: Minimum voltage regulator output (VAMIN) (< 0).  Typical value = -8.
    kb: Second stage regulator gain (KB) (> 0).  Typical value = 25.
    vrmax: Maximum voltage regulator outputs (VRMAX) (> 0).  Typical value = 105.
    vrmin: Minimum voltage regulator outputs (VRMIN) (< 0).  Typical value = -95.
    te: Exciter time constant, integration rate associated with exciter control (TE) (> 0).  Typical value = 0,6.
    vfemax: Exciter field current limit reference (VFEMAX) (> 0).  Typical value = 4,4.
    kh: Exciter field current feedback gain (KH) (>= 0).  Typical value = 1.
    kf: Excitation control system stabilizer gains (KF) (>= 0).  Typical value = 0,03.
    tf: Excitation control system stabilizer time constant (TF) (> 0).  Typical value = 1.
    kc: Rectifier loading factor proportional to commutating reactance (KC) (>= 0).  Typical value = 0,28.
    kd: Demagnetizing factor, a function of exciter alternator reactances (KD) (>= 0).  Typical value = 0,35.
    ke: Exciter constant related to self-excited field (KE) (>= 0).  Typical value = 1.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (VE1) (> 0).
      Typical value = 4,4.
    seve1: Exciter saturation function value at the corresponding exciter voltage, VE1, back of commutating reactance
      (SE[VE1]) (>= 0).  Typical value = 0,037.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (VE2) (> 0).
      Typical value = 3,3.
    seve2: Exciter saturation function value at the corresponding exciter voltage, VE2, back of commutating reactance
      (SE[VE2]) (>= 0).  Typical value = 0,012.
    """

    tb: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM
    ka: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    vamax: float = 0.0  # Type #PU in CIM
    vamin: float = 0.0  # Type #PU in CIM
    kb: float = 0.0  # Type #PU in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    te: int = 0  # Type #Seconds in CIM
    vfemax: float = 0.0  # Type #PU in CIM
    kh: float = 0.0  # Type #PU in CIM
    kf: float = 0.0  # Type #PU in CIM
    tf: int = 0  # Type #Seconds in CIM
    kc: float = 0.0  # Type #PU in CIM
    kd: float = 0.0  # Type #PU in CIM
    ke: float = 0.0  # Type #PU in CIM
    ve1: float = 0.0  # Type #PU in CIM
    seve1: float = 0.0  # Type #Float in CIM
    ve2: float = 0.0  # Type #PU in CIM
    seve2: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcIEEEAC2A"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
        }
