"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcAC8B(ExcitationSystemDynamics):
    """
    Modified IEEE AC8B alternator-supplied rectifier excitation system with speed input and input limiter.

    inlim: Input limiter indicator. true = input limiter Vimax and Vimin is considered false = input limiter Vimax and
      Vimin is not considered. Typical value = true.
    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 1.
    kc: Rectifier loading factor proportional to commutating reactance (Kc) (>= 0). Typical value = 0,55.
    kd: Demagnetizing factor, a function of exciter alternator reactances (Kd) (>= 0).  Typical value = 1,1.
    kdr: Voltage regulator derivative gain (Kdr) (>= 0).  Typical value = 10.
    ke: Exciter constant related to self-excited field (Ke).  Typical value = 1.
    kir: Voltage regulator integral gain (Kir) (>= 0).  Typical value = 5.
    kpr: Voltage regulator proportional gain (Kpr) (> 0 if ExcAC8B.kir = 0).  Typical value = 80.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical value = 0.
    pidlim: PID limiter indicator. true = input limiter Vpidmax and Vpidmin is considered false = input limiter Vpidmax
      and Vpidmin is not considered. Typical value = true.
    seve1: Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance
      (Se[Ve1]) (>= 0).  Typical value = 0,3.
    seve2: Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance
      (Se[Ve2]) (>= 0).  Typical value = 3.
    ta: Voltage regulator time constant (Ta) (>= 0).  Typical value = 0.
    tdr: Lag time constant (Tdr) (> 0 if ExcAC8B.kdr > 0).  Typical value = 0,1.
    te: Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 1,2.
    telim: Selector for the limiter on the block (1/sTe).  See diagram for meaning of true and false. Typical value =
      false.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1) (> 0).
      Typical value = 6,5.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2) (> 0).
      Typical value = 9.
    vemin: Minimum exciter voltage output (Vemin) (<= 0).  Typical value = 0.
    vfemax: Exciter field current limit reference (Vfemax).  Typical value = 6.
    vimax: Input signal maximum (Vimax) (> ExcAC8B.vimin).  Typical value = 35.
    vimin: Input signal minimum (Vimin) (< ExcAC8B.vimax).  Typical value = -10.
    vpidmax: PID maximum controller output (Vpidmax) (> ExcAC8B.vpidmin).  Typical value = 35.
    vpidmin: PID minimum controller output (Vpidmin) (< ExcAC8B.vpidmax).  Typical value = -10.
    vrmax: Maximum voltage regulator output (Vrmax) (> 0). Typical value = 35.
    vrmin: Minimum voltage regulator output (Vrmin) (< 0).  Typical value = 0.
    vtmult: Multiply by generator`s terminal voltage indicator. true =the limits Vrmax and Vrmin are multiplied by the
      generator`s terminal voltage to represent a thyristor power stage fed from the generator terminals
      false = limits are not multiplied by generator`s terminal voltage.  Typical value = false.
    """

    inlim: bool = False  # Type #Boolean in CIM
    ka: float = 0.0  # Type #PU in CIM
    kc: float = 0.0  # Type #PU in CIM
    kd: float = 0.0  # Type #PU in CIM
    kdr: float = 0.0  # Type #PU in CIM
    ke: float = 0.0  # Type #PU in CIM
    kir: float = 0.0  # Type #PU in CIM
    kpr: float = 0.0  # Type #PU in CIM
    ks: float = 0.0  # Type #PU in CIM
    pidlim: bool = False  # Type #Boolean in CIM
    seve1: float = 0.0  # Type #Float in CIM
    seve2: float = 0.0  # Type #Float in CIM
    ta: int = 0  # Type #Seconds in CIM
    tdr: int = 0  # Type #Seconds in CIM
    te: int = 0  # Type #Seconds in CIM
    telim: bool = False  # Type #Boolean in CIM
    ve1: float = 0.0  # Type #PU in CIM
    ve2: float = 0.0  # Type #PU in CIM
    vemin: float = 0.0  # Type #PU in CIM
    vfemax: float = 0.0  # Type #PU in CIM
    vimax: float = 0.0  # Type #PU in CIM
    vimin: float = 0.0  # Type #PU in CIM
    vpidmax: float = 0.0  # Type #PU in CIM
    vpidmin: float = 0.0  # Type #PU in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    vtmult: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcAC8B"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "inlim": [
                Profile.DY.value,
            ],
            "ka": [
                Profile.DY.value,
            ],
            "kc": [
                Profile.DY.value,
            ],
            "kd": [
                Profile.DY.value,
            ],
            "kdr": [
                Profile.DY.value,
            ],
            "ke": [
                Profile.DY.value,
            ],
            "kir": [
                Profile.DY.value,
            ],
            "kpr": [
                Profile.DY.value,
            ],
            "ks": [
                Profile.DY.value,
            ],
            "pidlim": [
                Profile.DY.value,
            ],
            "seve1": [
                Profile.DY.value,
            ],
            "seve2": [
                Profile.DY.value,
            ],
            "ta": [
                Profile.DY.value,
            ],
            "tdr": [
                Profile.DY.value,
            ],
            "te": [
                Profile.DY.value,
            ],
            "telim": [
                Profile.DY.value,
            ],
            "ve1": [
                Profile.DY.value,
            ],
            "ve2": [
                Profile.DY.value,
            ],
            "vemin": [
                Profile.DY.value,
            ],
            "vfemax": [
                Profile.DY.value,
            ],
            "vimax": [
                Profile.DY.value,
            ],
            "vimin": [
                Profile.DY.value,
            ],
            "vpidmax": [
                Profile.DY.value,
            ],
            "vpidmin": [
                Profile.DY.value,
            ],
            "vrmax": [
                Profile.DY.value,
            ],
            "vrmin": [
                Profile.DY.value,
            ],
            "vtmult": [
                Profile.DY.value,
            ],
        }
