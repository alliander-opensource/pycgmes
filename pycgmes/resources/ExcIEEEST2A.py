"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcIEEEST2A(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type ST2A model. Some static systems use both current and voltage sources (generator terminal
      quantities) to comprise the power source.  The regulator controls the exciter output through controlled
      saturation of the power transformer components.  These compound-source rectifier excitation systems are
      designated type ST2A and are represented by ExcIEEEST2A. Reference: IEEE 421.5-2005, 7.2.

    ka: Voltage regulator gain (KA) (> 0).  Typical value = 120.
    ta: Voltage regulator time constant (TA) (> 0).  Typical value = 0,15.
    vrmax: Maximum voltage regulator outputs (VRMAX) (> 0).  Typical value = 1.
    vrmin: Minimum voltage regulator outputs (VRMIN) (<= 0).  Typical value = 0.
    ke: Exciter constant related to self-excited field (KE).  Typical value = 1.
    te: Exciter time constant, integration rate associated with exciter control (TE) (> 0).  Typical value = 0,5.
    kf: Excitation control system stabilizer gains (KF) (>= 0).  Typical value = 0,05.
    tf: Excitation control system stabilizer time constant (TF) (>= 0).  Typical value = 1.
    kp: Potential circuit gain coefficient (KP) (>= 0).  Typical value = 4,88.
    ki: Potential circuit gain coefficient (KI) (>= 0).  Typical value = 8.
    kc: Rectifier loading factor proportional to commutating reactance (KC) (>= 0). Typical value = 1,82.
    efdmax: Maximum field voltage (EFDMax) (>= 0).  Typical value = 99.
    uelin: UEL input (UELin). true = HV gate false = add to error signal. Typical value = true.
    """

    ka: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    ke: float = 0.0  # Type #PU in CIM
    te: int = 0  # Type #Seconds in CIM
    kf: float = 0.0  # Type #PU in CIM
    tf: int = 0  # Type #Seconds in CIM
    kp: float = 0.0  # Type #PU in CIM
    ki: float = 0.0  # Type #PU in CIM
    kc: float = 0.0  # Type #PU in CIM
    efdmax: float = 0.0  # Type #PU in CIM
    uelin: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcIEEEST2A"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "vrmax": [
                Profile.DY.value,
            ],
            "vrmin": [
                Profile.DY.value,
            ],
            "ke": [
                Profile.DY.value,
            ],
            "te": [
                Profile.DY.value,
            ],
            "kf": [
                Profile.DY.value,
            ],
            "tf": [
                Profile.DY.value,
            ],
            "kp": [
                Profile.DY.value,
            ],
            "ki": [
                Profile.DY.value,
            ],
            "kc": [
                Profile.DY.value,
            ],
            "efdmax": [
                Profile.DY.value,
            ],
            "uelin": [
                Profile.DY.value,
            ],
        }
