"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

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

    efdmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    efdmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    emax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    emin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k1: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    k2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kc: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kce: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kd: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kgob: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kqi: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kqob: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kqp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    nq: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    qconoff: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    qz: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    remote: bool = Field(
        default=False,
        in_profiles=[
            Profile.DY,
        ],
    )

    sbase: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tc: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    te: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ti: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tp: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tr: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    uimax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    uimin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    urmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    urmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vtmax: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    vtmin: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    yp: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }
