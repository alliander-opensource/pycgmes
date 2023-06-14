"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcSK(ExcitationSystemDynamics):
    """
    Slovakian excitation system.  UEL and secondary voltage control are included in this model. When this model is used,
      there cannot be a separate underexcitation limiter or VAr controller model.

    efdmax: Field voltage clipping upper level limit (Efdmax) (> ExcSK.efdmin).
    efdmin: Field voltage clipping lower level limit (Efdmin) (< ExcSK.efdmax).
    emax: Maximum field voltage output (Emax) (> ExcSK.emin).  Typical value = 20.
    emin: Minimum field voltage output (Emin) (< ExcSK.emax).  Typical value = -20.
    k: Gain (K).  Typical value = 1.
    k1: Parameter of underexcitation limit (K1).  Typical value = 0,1364.
    k2: Parameter of underexcitation limit (K2).  Typical value = -0,3861.
    kc: PI controller gain (Kc).  Typical value = 70.
    kce: Rectifier regulation factor (Kce).  Typical value = 0.
    kd: Exciter internal reactance (Kd).  Typical value = 0.
    kgob: P controller gain (Kgob).  Typical value = 10.
    kp: PI controller gain (Kp).  Typical value = 1.
    kqi: PI controller gain of integral component (Kqi).  Typical value = 0.
    kqob: Rate of rise of the reactive power (Kqob).
    kqp: PI controller gain (Kqp).  Typical value = 0.
    nq: Deadband of reactive power (nq).  Determines the range of sensitivity.  Typical value = 0,001.
    qconoff: Secondary voltage control state (Qc_on_off). true = secondary voltage control is on false = secondary
      voltage control is off. Typical value = false.
    qz: Desired value (setpoint) of reactive power, manual setting (Qz).
    remote: Selector to apply automatic calculation in secondary controller model (remote). true = automatic calculation
      is activated false = manual set is active; the use of desired value of reactive power (Qz) is
      required. Typical value = true.
    sbase: Apparent power of the unit (Sbase) (> 0).  Unit = MVA.  Typical value = 259.
    tc: PI controller phase lead time constant (Tc) (>= 0).  Typical value = 8.
    te: Time constant of gain block (Te) (>= 0).  Typical value = 0,1.
    ti: PI controller phase lead time constant (Ti) (>= 0).  Typical value = 2.
    tp: Time constant (Tp) (>= 0).  Typical value = 0,1.
    tr: Voltage transducer time constant (Tr) (>= 0).  Typical value = 0,01.
    uimax: Maximum error (UImax) (> ExcSK.uimin).  Typical value = 10.
    uimin: Minimum error (UImin) (< ExcSK.uimax).  Typical value = -10.
    urmax: Maximum controller output (URmax) (> ExcSK.urmin).  Typical value = 10.
    urmin: Minimum controller output (URmin) (< ExcSK.urmax).  Typical value = -10.
    vtmax: Maximum terminal voltage input (Vtmax) (> ExcSK.vtmin).  Determines the range of voltage deadband.  Typical
      value = 1,05.
    vtmin: Minimum terminal voltage input (Vtmin) (< ExcSK.vtmax).  Determines the range of voltage deadband.  Typical
      value = 0,95.
    yp: Maximum output (Yp).  Typical value = 1.
    """

    efdmax: float = 0.0  # Type #PU in CIM
    efdmin: float = 0.0  # Type #PU in CIM
    emax: float = 0.0  # Type #PU in CIM
    emin: float = 0.0  # Type #PU in CIM
    k: float = 0.0  # Type #PU in CIM
    k1: float = 0.0  # Type #PU in CIM
    k2: float = 0.0  # Type #PU in CIM
    kc: float = 0.0  # Type #PU in CIM
    kce: float = 0.0  # Type #PU in CIM
    kd: float = 0.0  # Type #PU in CIM
    kgob: float = 0.0  # Type #PU in CIM
    kp: float = 0.0  # Type #PU in CIM
    kqi: float = 0.0  # Type #PU in CIM
    kqob: float = 0.0  # Type #PU in CIM
    kqp: float = 0.0  # Type #PU in CIM
    nq: float = 0.0  # Type #PU in CIM
    qconoff: bool = False  # Type #Boolean in CIM
    qz: float = 0.0  # Type #PU in CIM
    remote: bool = False  # Type #Boolean in CIM
    sbase: float = 0.0  # Type #ApparentPower in CIM
    tc: int = 0  # Type #Seconds in CIM
    te: int = 0  # Type #Seconds in CIM
    ti: int = 0  # Type #Seconds in CIM
    tp: int = 0  # Type #Seconds in CIM
    tr: int = 0  # Type #Seconds in CIM
    uimax: float = 0.0  # Type #PU in CIM
    uimin: float = 0.0  # Type #PU in CIM
    urmax: float = 0.0  # Type #PU in CIM
    urmin: float = 0.0  # Type #PU in CIM
    vtmax: float = 0.0  # Type #PU in CIM
    vtmin: float = 0.0  # Type #PU in CIM
    yp: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcSK"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "efdmax": [
                Profile.DY.value,
            ],
            "efdmin": [
                Profile.DY.value,
            ],
            "emax": [
                Profile.DY.value,
            ],
            "emin": [
                Profile.DY.value,
            ],
            "k": [
                Profile.DY.value,
            ],
            "k1": [
                Profile.DY.value,
            ],
            "k2": [
                Profile.DY.value,
            ],
            "kc": [
                Profile.DY.value,
            ],
            "kce": [
                Profile.DY.value,
            ],
            "kd": [
                Profile.DY.value,
            ],
            "kgob": [
                Profile.DY.value,
            ],
            "kp": [
                Profile.DY.value,
            ],
            "kqi": [
                Profile.DY.value,
            ],
            "kqob": [
                Profile.DY.value,
            ],
            "kqp": [
                Profile.DY.value,
            ],
            "nq": [
                Profile.DY.value,
            ],
            "qconoff": [
                Profile.DY.value,
            ],
            "qz": [
                Profile.DY.value,
            ],
            "remote": [
                Profile.DY.value,
            ],
            "sbase": [
                Profile.DY.value,
            ],
            "tc": [
                Profile.DY.value,
            ],
            "te": [
                Profile.DY.value,
            ],
            "ti": [
                Profile.DY.value,
            ],
            "tp": [
                Profile.DY.value,
            ],
            "tr": [
                Profile.DY.value,
            ],
            "uimax": [
                Profile.DY.value,
            ],
            "uimin": [
                Profile.DY.value,
            ],
            "urmax": [
                Profile.DY.value,
            ],
            "urmin": [
                Profile.DY.value,
            ],
            "vtmax": [
                Profile.DY.value,
            ],
            "vtmin": [
                Profile.DY.value,
            ],
            "yp": [
                Profile.DY.value,
            ],
        }
