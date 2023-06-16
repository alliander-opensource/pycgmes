"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from typing import Optional
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcST6B(ExcitationSystemDynamics):
    """
    Modified IEEE ST6B static excitation system with PID controller and optional inner feedback loop.

    ilr: Exciter output current limit reference (Ilr) (> 0).  Typical value = 4,164.
    k1: Selector (K1). true = feedback is from Ifd false = feedback is not from Ifd. Typical value = true.
    kcl: Exciter output current limit adjustment (Kcl) (> 0).  Typical value = 1,0577.
    kff: Pre-control gain constant of the inner loop field regulator (Kff).  Typical value = 1.
    kg: Feedback gain constant of the inner loop field regulator (Kg) (>= 0).  Typical value = 1.
    kia: Voltage regulator integral gain (Kia) (> 0).  Typical value = 45,094.
    klr: Exciter output current limit adjustment (Kcl) (> 0).  Typical value = 17,33.
    km: Forward gain constant of the inner loop field regulator (Km).  Typical value = 1.
    kpa: Voltage regulator proportional gain (Kpa) (> 0).  Typical value = 18,038.
    kvd: Voltage regulator derivative gain (Kvd).  Typical value = 0.
    oelin: OEL input selector (OELin).  Typical value = noOELinput (corresponds to OELin = 0 on diagram).
    tg: Feedback time constant of inner loop field voltage regulator (Tg) (>= 0).  Typical value = 0,02.
    ts: Rectifier firing time constant (Ts) (>= 0).  Typical value = 0.
    tvd: Voltage regulator derivative gain (Tvd) (>= 0).  Typical value = 0.
    vamax: Maximum voltage regulator output (Vamax) (> 0).  Typical value = 4,81.
    vamin: Minimum voltage regulator output (Vamin) (< 0).  Typical value = -3,85.
    vilim: Selector (Vilim). true = Vimin-Vimax limiter is active false = Vimin-Vimax limiter is not active. Typical
      value = true.
    vimax: Maximum voltage regulator input limit (Vimax) (> ExcST6B.vimin).  Typical value = 10.
    vimin: Minimum voltage regulator input limit (Vimin) (< ExcST6B.vimax).  Typical value = -10.
    vmult: Selector (vmult). true = multiply regulator output by terminal voltage false = do not multiply regulator
      output by terminal voltage.  Typical value = true.
    vrmax: Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 4,81.
    vrmin: Minimum voltage regulator output (Vrmin) (< 0).  Typical value = -3,85.
    xc: Excitation source reactance (Xc).  Typical value = 0,05.
    """

    ilr: float = 0.0  # Type #PU in CIM
    k1: bool = False  # Type #Boolean in CIM
    kcl: float = 0.0  # Type #PU in CIM
    kff: float = 0.0  # Type #PU in CIM
    kg: float = 0.0  # Type #PU in CIM
    kia: float = 0.0  # Type #PU in CIM
    klr: float = 0.0  # Type #PU in CIM
    km: float = 0.0  # Type #PU in CIM
    kpa: float = 0.0  # Type #PU in CIM
    kvd: float = 0.0  # Type #PU in CIM
    oelin: Optional[str] = None  # Type M:1..1 in CIM
    tg: int = 0  # Type #Seconds in CIM
    ts: int = 0  # Type #Seconds in CIM
    tvd: int = 0  # Type #Seconds in CIM
    vamax: float = 0.0  # Type #PU in CIM
    vamin: float = 0.0  # Type #PU in CIM
    vilim: bool = False  # Type #Boolean in CIM
    vimax: float = 0.0  # Type #PU in CIM
    vimin: float = 0.0  # Type #PU in CIM
    vmult: bool = False  # Type #Boolean in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    xc: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcST6B"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "ilr": [
                Profile.DY.value,
            ],
            "k1": [
                Profile.DY.value,
            ],
            "kcl": [
                Profile.DY.value,
            ],
            "kff": [
                Profile.DY.value,
            ],
            "kg": [
                Profile.DY.value,
            ],
            "kia": [
                Profile.DY.value,
            ],
            "klr": [
                Profile.DY.value,
            ],
            "km": [
                Profile.DY.value,
            ],
            "kpa": [
                Profile.DY.value,
            ],
            "kvd": [
                Profile.DY.value,
            ],
            "oelin": [
                Profile.DY.value,
            ],
            "tg": [
                Profile.DY.value,
            ],
            "ts": [
                Profile.DY.value,
            ],
            "tvd": [
                Profile.DY.value,
            ],
            "vamax": [
                Profile.DY.value,
            ],
            "vamin": [
                Profile.DY.value,
            ],
            "vilim": [
                Profile.DY.value,
            ],
            "vimax": [
                Profile.DY.value,
            ],
            "vimin": [
                Profile.DY.value,
            ],
            "vmult": [
                Profile.DY.value,
            ],
            "vrmax": [
                Profile.DY.value,
            ],
            "vrmin": [
                Profile.DY.value,
            ],
            "xc": [
                Profile.DY.value,
            ],
        }
