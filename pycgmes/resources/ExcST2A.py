"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
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

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

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
        str_ = "class=ExcST2A\n"
        attributes = self.__dict__
        for key, val in attributes.items():
            str_ = str_ + key + f"={val}\n"
        return str_

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                self.profiles.DY.value,
            ],
            # Attributes
            "ka": [
                self.profiles.DY.value,
            ],
            "ta": [
                self.profiles.DY.value,
            ],
            "vrmax": [
                self.profiles.DY.value,
            ],
            "vrmin": [
                self.profiles.DY.value,
            ],
            "ke": [
                self.profiles.DY.value,
            ],
            "te": [
                self.profiles.DY.value,
            ],
            "kf": [
                self.profiles.DY.value,
            ],
            "tf": [
                self.profiles.DY.value,
            ],
            "kp": [
                self.profiles.DY.value,
            ],
            "ki": [
                self.profiles.DY.value,
            ],
            "kc": [
                self.profiles.DY.value,
            ],
            "efdmax": [
                self.profiles.DY.value,
            ],
            "uelin": [
                self.profiles.DY.value,
            ],
            "tb": [
                self.profiles.DY.value,
            ],
            "tc": [
                self.profiles.DY.value,
            ],
        }
