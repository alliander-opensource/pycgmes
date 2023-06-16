"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
class ExcST2A(ExcitationSystemDynamics):
    """
    Modified IEEE ST2A static excitation system with another lead-lag block added to match the model defined by WECC.

    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 120.
    ta: Voltage regulator time constant (Ta) (> 0).  Typical value = 0,15.
    vrmax: Maximum voltage regulator outputs (Vrmax) (> 0).  Typical value = 1.
    vrmin: Minimum voltage regulator outputs (Vrmin) (< 0).  Typical value = -1.
    ke: Exciter constant related to self-excited field (Ke).  Typical value = 1.
    te: Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 0,5.
    kf: Excitation control system stabilizer gains (kf) (>= 0).  Typical value = 0,05.
    tf: Excitation control system stabilizer time constant (Tf) (>= 0).  Typical value = 0,7.
    kp: Potential circuit gain coefficient (Kp) (>= 0).  Typical value = 4,88.
    ki: Potential circuit gain coefficient (Ki) (>= 0).  Typical value = 8.
    kc: Rectifier loading factor proportional to commutating reactance (Kc) (>= 0).  Typical value = 1,82.
    efdmax: Maximum field voltage (Efdmax) (>= 0).  Typical value = 99.
    uelin: UEL input (UELin). true = HV gate false = add to error signal. Typical value = false.
    tb: Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.
    tc: Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.
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
    tb: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=ExcST2A"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "tb": [
                Profile.DY.value,
            ],
            "tc": [
                Profile.DY.value,
            ],
        }
