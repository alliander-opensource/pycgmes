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
class ExcIEEEST1A(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type ST1A model. This model represents systems in which excitation power is supplied through a
      transformer from the generator terminals (or the unit's auxiliary bus) and is regulated by a controlled
      rectifier.  The maximum exciter voltage available from such systems is directly related to the generator
      terminal voltage. Reference: IEEE 421.5-2005, 7.1.

    ilr: Exciter output current limit reference (ILR).  Typical value = 0.
    ka: Voltage regulator gain (KA) (> 0).  Typical value = 190.
    kc: Rectifier loading factor proportional to commutating reactance (KC) (>= 0). Typical value = 0,08.
    kf: Excitation control system stabilizer gains (KF) (>= 0).  Typical value = 0.
    klr: Exciter output current limiter gain (KLR).  Typical value = 0.
    pssin: Selector of the Power System Stabilizer (PSS) input (PSSin). true = PSS input (Vs) added to error signal
      false = PSS input (Vs) added to voltage regulator output. Typical value = true.
    ta: Voltage regulator time constant (TA) (>= 0).  Typical value = 0.
    tb: Voltage regulator time constant (TB) (>= 0).  Typical value = 10.
    tb1: Voltage regulator time constant (TB1) (>= 0).  Typical value = 0.
    tc: Voltage regulator time constant (TC) (>= 0).  Typical value = 1.
    tc1: Voltage regulator time constant (TC1) (>= 0).  Typical value = 0.
    tf: Excitation control system stabilizer time constant (TF) (>= 0).  Typical value = 1.
    uelin: Selector of the connection of the UEL input (UELin).  Typical value = ignoreUELsignal.
    vamax: Maximum voltage regulator output (VAMAX) (> 0).  Typical value = 14,5.
    vamin: Minimum voltage regulator output (VAMIN) (< 0).  Typical value = -14,5.
    vimax: Maximum voltage regulator input limit (VIMAX) (> 0).  Typical value = 999.
    vimin: Minimum voltage regulator input limit (VIMIN) (< 0).  Typical value = -999.
    vrmax: Maximum voltage regulator outputs (VRMAX) (> 0).  Typical value = 7,8.
    vrmin: Minimum voltage regulator outputs (VRMIN) (< 0).  Typical value = -6,7.
    """

    ilr: float = 0.0  # Type #PU in CIM
    ka: float = 0.0  # Type #PU in CIM
    kc: float = 0.0  # Type #PU in CIM
    kf: float = 0.0  # Type #PU in CIM
    klr: float = 0.0  # Type #PU in CIM
    pssin: bool = False  # Type #Boolean in CIM
    ta: int = 0  # Type #Seconds in CIM
    tb: int = 0  # Type #Seconds in CIM
    tb1: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM
    tc1: int = 0  # Type #Seconds in CIM
    tf: int = 0  # Type #Seconds in CIM
    uelin: Optional[str] = None  # Type M:1..1 in CIM
    vamax: float = 0.0  # Type #PU in CIM
    vamin: float = 0.0  # Type #PU in CIM
    vimax: float = 0.0  # Type #PU in CIM
    vimin: float = 0.0  # Type #PU in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcIEEEST1A"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "ka": [
                Profile.DY.value,
            ],
            "kc": [
                Profile.DY.value,
            ],
            "kf": [
                Profile.DY.value,
            ],
            "klr": [
                Profile.DY.value,
            ],
            "pssin": [
                Profile.DY.value,
            ],
            "ta": [
                Profile.DY.value,
            ],
            "tb": [
                Profile.DY.value,
            ],
            "tb1": [
                Profile.DY.value,
            ],
            "tc": [
                Profile.DY.value,
            ],
            "tc1": [
                Profile.DY.value,
            ],
            "tf": [
                Profile.DY.value,
            ],
            "uelin": [
                Profile.DY.value,
            ],
            "vamax": [
                Profile.DY.value,
            ],
            "vamin": [
                Profile.DY.value,
            ],
            "vimax": [
                Profile.DY.value,
            ],
            "vimin": [
                Profile.DY.value,
            ],
            "vrmax": [
                Profile.DY.value,
            ],
            "vrmin": [
                Profile.DY.value,
            ],
        }
