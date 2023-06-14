"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcIEEEAC8B(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type AC8B model. This model represents a PID voltage regulator with either a brushless exciter or DC
      exciter. The AVR in this model consists of PID control, with separate constants for the proportional (KPR),
      integral (KIR), and derivative (KDR) gains. The representation of the brushless exciter (TE, KE, SE, KC, KD)
      is similar to the model type AC2A. The type AC8B model can be used to represent static voltage regulators
      applied to brushless excitation systems. Digitally based voltage regulators feeding DC rotating main exciters
      can be represented with the AC type AC8B model with the parameters KC and KD set to 0.  For thyristor power
      stages fed from the generator terminals, the limits VRMAX and VRMIN should be a function of terminal voltage:
      VT x VRMAX and VT x VRMIN. Reference: IEEE 421.5-2005, 6.8.

    kpr: Voltage regulator proportional gain (KPR) (> 0 if ExcIEEEAC8B.kir = 0).  Typical value = 80.
    kir: Voltage regulator integral gain (KIR) (>= 0).  Typical value = 5.
    kdr: Voltage regulator derivative gain (KDR) (>= 0).  Typical value = 10.
    tdr: Lag time constant (TDR) (> 0).  Typical value = 0,1.
    vrmax: Maximum voltage regulator output (VRMAX) (> 0).  Typical value = 35.
    vrmin: Minimum voltage regulator output (VRMIN) (<= 0).  Typical value = 0.
    ka: Voltage regulator gain (KA) (> 0).  Typical value = 1.
    ta: Voltage regulator time constant (TA) (>= 0).  Typical value = 0.
    te: Exciter time constant, integration rate associated with exciter control (TE) (> 0).  Typical value = 1,2.
    vfemax: Exciter field current limit reference (VFEMAX).  Typical value = 6.
    vemin: Minimum exciter voltage output (VEMIN) (<= 0).  Typical value = 0.
    ke: Exciter constant related to self-excited field (KE).  Typical value = 1.
    kc: Rectifier loading factor proportional to commutating reactance (KC) (>= 0). Typical value = 0,55.
    kd: Demagnetizing factor, a function of exciter alternator reactances (KD) (>= 0).  Typical value = 1,1.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (VE1) (> 0).
      Typical value = 6,5.
    seve1: Exciter saturation function value at the corresponding exciter voltage, VE1, back of commutating reactance
      (SE[VE1]) (>= 0).  Typical value = 0,3.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (VE2) (> 0).
      Typical value = 9.
    seve2: Exciter saturation function value at the corresponding exciter voltage, VE2, back of commutating reactance
      (SE[VE2]) (>= 0).  Typical value = 3.
    """

    kpr: float = 0.0  # Type #PU in CIM
    kir: float = 0.0  # Type #PU in CIM
    kdr: float = 0.0  # Type #PU in CIM
    tdr: int = 0  # Type #Seconds in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    ka: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    te: int = 0  # Type #Seconds in CIM
    vfemax: float = 0.0  # Type #PU in CIM
    vemin: float = 0.0  # Type #PU in CIM
    ke: float = 0.0  # Type #PU in CIM
    kc: float = 0.0  # Type #PU in CIM
    kd: float = 0.0  # Type #PU in CIM
    ve1: float = 0.0  # Type #PU in CIM
    seve1: float = 0.0  # Type #Float in CIM
    ve2: float = 0.0  # Type #PU in CIM
    seve2: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcIEEEAC8B"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "kpr": [
                Profile.DY.value,
            ],
            "kir": [
                Profile.DY.value,
            ],
            "kdr": [
                Profile.DY.value,
            ],
            "tdr": [
                Profile.DY.value,
            ],
            "vrmax": [
                Profile.DY.value,
            ],
            "vrmin": [
                Profile.DY.value,
            ],
            "ka": [
                Profile.DY.value,
            ],
            "ta": [
                Profile.DY.value,
            ],
            "te": [
                Profile.DY.value,
            ],
            "vfemax": [
                Profile.DY.value,
            ],
            "vemin": [
                Profile.DY.value,
            ],
            "ke": [
                Profile.DY.value,
            ],
            "kc": [
                Profile.DY.value,
            ],
            "kd": [
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
