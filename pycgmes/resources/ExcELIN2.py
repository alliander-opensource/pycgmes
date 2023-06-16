"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcELIN2(ExcitationSystemDynamics):
    """
    Detailed excitation system ELIN (VATECH).  This model represents an all-static excitation system. A PI voltage
      controller establishes a desired field current set point for a proportional current controller. The integrator
      of the PI controller has a follow-up input to match its signal to the present field current.  Power system
      stabilizer models used in conjunction with this excitation system model: PssELIN2, PssIEEE2B, Pss2B.

    k1: Voltage regulator input gain (K1).  Typical value = 0.
    k1ec: Voltage regulator input limit (K1ec).  Typical value = 2.
    kd1: Voltage controller derivative gain (Kd1).  Typical value = 34,5.
    tb1: Voltage controller derivative washout time constant (Tb1) (>= 0).  Typical value = 12,45.
    pid1max: Controller follow up gain (PID1max).  Typical value = 2.
    ti1: Controller follow up deadband (Ti1).  Typical value = 0.
    iefmax2: Minimum open circuit excitation voltage (Iefmax2).  Typical value = -5.
    k2: Gain (K2).  Typical value = 5.
    ketb: Gain (Ketb).  Typical value = 0,06.
    upmax: Limiter (Upmax) (> ExcELIN2.upmin).  Typical value = 3.
    upmin: Limiter (Upmin) (< ExcELIN2.upmax).  Typical value = 0.
    te: Time constant (Te) (>= 0).  Typical value = 0.
    xp: Excitation transformer effective reactance (Xp).  Typical value = 1.
    te2: Time Constant (Te2) (>= 0).  Typical value = 1.
    ke2: Gain (Ke2).  Typical value = 0,1.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1) (> 0).
      Typical value = 3.
    seve1: Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance
      (Se[Ve1]) (>= 0).  Typical value = 0.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2) (> 0).
      Typical value = 0.
    seve2: Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance
      (Se[Ve2]) (>= 0).  Typical value = 1.
    tr4: Time constant (Tr4) (>= 0).  Typical value = 1.
    k3: Gain (K3).  Typical value = 0,1.
    ti3: Time constant (Ti3) (>= 0).  Typical value = 3.
    k4: Gain (K4).  Typical value = 0.
    ti4: Time constant (Ti4) (>= 0).  Typical value = 0.
    iefmax: Limiter (Iefmax) (> ExcELIN2.iefmin).  Typical value = 1.
    iefmin: Limiter (Iefmin) (< ExcELIN2.iefmax).  Typical value = 1.
    efdbas: Gain (Efdbas).  Typical value = 0,1.
    """

    k1: float = 0.0  # Type #PU in CIM
    k1ec: float = 0.0  # Type #PU in CIM
    kd1: float = 0.0  # Type #PU in CIM
    tb1: int = 0  # Type #Seconds in CIM
    pid1max: float = 0.0  # Type #PU in CIM
    ti1: float = 0.0  # Type #PU in CIM
    iefmax2: float = 0.0  # Type #PU in CIM
    k2: float = 0.0  # Type #PU in CIM
    ketb: float = 0.0  # Type #PU in CIM
    upmax: float = 0.0  # Type #PU in CIM
    upmin: float = 0.0  # Type #PU in CIM
    te: int = 0  # Type #Seconds in CIM
    xp: float = 0.0  # Type #PU in CIM
    te2: int = 0  # Type #Seconds in CIM
    ke2: float = 0.0  # Type #PU in CIM
    ve1: float = 0.0  # Type #PU in CIM
    seve1: float = 0.0  # Type #PU in CIM
    ve2: float = 0.0  # Type #PU in CIM
    seve2: float = 0.0  # Type #PU in CIM
    tr4: int = 0  # Type #Seconds in CIM
    k3: float = 0.0  # Type #PU in CIM
    ti3: int = 0  # Type #Seconds in CIM
    k4: float = 0.0  # Type #PU in CIM
    ti4: int = 0  # Type #Seconds in CIM
    iefmax: float = 0.0  # Type #PU in CIM
    iefmin: float = 0.0  # Type #PU in CIM
    efdbas: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcELIN2"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "k1": [
                Profile.DY.value,
            ],
            "k1ec": [
                Profile.DY.value,
            ],
            "kd1": [
                Profile.DY.value,
            ],
            "tb1": [
                Profile.DY.value,
            ],
            "pid1max": [
                Profile.DY.value,
            ],
            "ti1": [
                Profile.DY.value,
            ],
            "iefmax2": [
                Profile.DY.value,
            ],
            "k2": [
                Profile.DY.value,
            ],
            "ketb": [
                Profile.DY.value,
            ],
            "upmax": [
                Profile.DY.value,
            ],
            "upmin": [
                Profile.DY.value,
            ],
            "te": [
                Profile.DY.value,
            ],
            "xp": [
                Profile.DY.value,
            ],
            "te2": [
                Profile.DY.value,
            ],
            "ke2": [
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
            "tr4": [
                Profile.DY.value,
            ],
            "k3": [
                Profile.DY.value,
            ],
            "ti3": [
                Profile.DY.value,
            ],
            "k4": [
                Profile.DY.value,
            ],
            "ti4": [
                Profile.DY.value,
            ],
            "iefmax": [
                Profile.DY.value,
            ],
            "iefmin": [
                Profile.DY.value,
            ],
            "efdbas": [
                Profile.DY.value,
            ],
        }
