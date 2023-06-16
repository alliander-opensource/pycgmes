"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcIEEEAC6A(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type AC6A model. The model represents field-controlled alternator-rectifier excitation systems with
      system-supplied electronic voltage regulators.  The maximum output of the regulator, VR, is a function of
      terminal voltage, VT. The field current limiter included in the original model AC6A remains in the 2005
      update. Reference: IEEE 421.5-2005, 6.6.

    ka: Voltage regulator gain (KA) (> 0).  Typical value = 536.
    ta: Voltage regulator time constant (TA) (>= 0).  Typical value = 0,086.
    tk: Voltage regulator time constant (TK) (>= 0).  Typical value = 0,18.
    tb: Voltage regulator time constant (TB) (>= 0).  Typical value = 9.
    tc: Voltage regulator time constant (TC) (>= 0).  Typical value = 3.
    vamax: Maximum voltage regulator output (VAMAX) (> 0).  Typical value = 75.
    vamin: Minimum voltage regulator output (VAMIN) (< 0).  Typical value = -75.
    vrmax: Maximum voltage regulator output (VRMAX) (> 0).  Typical value = 44.
    vrmin: Minimum voltage regulator output (VRMIN) (< 0).  Typical value = -36.
    te: Exciter time constant, integration rate associated with exciter control (TE) (> 0).  Typical value = 1.
    kh: Exciter field current limiter gain (KH) (>= 0).  Typical value = 92.
    tj: Exciter field current limiter time constant (TJ) (>= 0).  Typical value = 0,02.
    th: Exciter field current limiter time constant (TH) (> 0).  Typical value = 0,08.
    vfelim: Exciter field current limit reference (VFELIM) (> 0).  Typical value = 19.
    vhmax: Maximum field current limiter signal reference (VHMAX) (> 0).  Typical value = 75.
    kc: Rectifier loading factor proportional to commutating reactance (KC) (>= 0). Typical value = 0,173.
    kd: Demagnetizing factor, a function of exciter alternator reactances (KD) (>= 0).  Typical value = 1,91.
    ke: Exciter constant related to self-excited field (KE).  Typical value = 1,6.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (VE1) (> 0).
      Typical value = 7,4.
    seve1: Exciter saturation function value at the corresponding exciter voltage, VE1, back of commutating reactance
      (SE[VE1]) (>= 0).  Typical value = 0,214.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (VE2) (> 0).
      Typical value = 5,55.
    seve2: Exciter saturation function value at the corresponding exciter voltage, VE2, back of commutating reactance
      (SE[VE2]) (>= 0).  Typical value = 0,044.
    """

    ka: float = 0.0  # Type #PU in CIM
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

        return "\n".join(
            ["class=ExcIEEEAC6A"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "ka": [
                Profile.DY.value,
            ],
            "ta": [
                Profile.DY.value,
            ],
            "tk": [
                Profile.DY.value,
            ],
            "tb": [
                Profile.DY.value,
            ],
            "tc": [
                Profile.DY.value,
            ],
            "vamax": [
                Profile.DY.value,
            ],
            "vamin": [
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
            "kh": [
                Profile.DY.value,
            ],
            "tj": [
                Profile.DY.value,
            ],
            "th": [
                Profile.DY.value,
            ],
            "vfelim": [
                Profile.DY.value,
            ],
            "vhmax": [
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
