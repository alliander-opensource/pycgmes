"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcST1A(ExcitationSystemDynamics):
    """
    Modification of an old IEEE ST1A static excitation system without overexcitation limiter (OEL) and underexcitation
      limiter (UEL).

    vimax: Maximum voltage regulator input limit (Vimax) (> 0).  Typical value = 999.
    vimin: Minimum voltage regulator input limit (Vimin) (< 0).  Typical value = -999.
    tc: Voltage regulator time constant (Tc) (>= 0).  Typical value = 1.
    tb: Voltage regulator time constant (Tb) (>= 0).  Typical value = 10.
    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 190.
    ta: Voltage regulator time constant (Ta) (>= 0).  Typical value = 0,02.
    vrmax: Maximum voltage regulator outputs (Vrmax) (> 0) .  Typical value = 7,8.
    vrmin: Minimum voltage regulator outputs (Vrmin) (< 0).  Typical value = -6,7.
    kc: Rectifier loading factor proportional to commutating reactance (Kc) (>= 0). Typical value = 0,05.
    kf: Excitation control system stabilizer gains (Kf) (>= 0).  Typical value = 0.
    tf: Excitation control system stabilizer time constant (Tf) (>= 0).  Typical value = 1.
    tc1: Voltage regulator time constant (Tc1) (>= 0).  Typical value = 0.
    tb1: Voltage regulator time constant (Tb1) (>= 0).  Typical value = 0.
    vamax: Maximum voltage regulator output (Vamax) (> 0).  Typical value = 999.
    vamin: Minimum voltage regulator output (Vamin) (< 0).  Typical value = -999.
    ilr: Exciter output current limit reference (Ilr).  Typical value = 0.
    klr: Exciter output current limiter gain (Klr).  Typical value = 0.
    xe: Excitation xfmr effective reactance (Xe).  Typical value = 0,04.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    vimax: float = 0.0  # Type #PU in CIM
    vimin: float = 0.0  # Type #PU in CIM
    tc: int = 0  # Type #Seconds in CIM
    tb: int = 0  # Type #Seconds in CIM
    ka: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    kc: float = 0.0  # Type #PU in CIM
    kf: float = 0.0  # Type #PU in CIM
    tf: int = 0  # Type #Seconds in CIM
    tc1: int = 0  # Type #Seconds in CIM
    tb1: int = 0  # Type #Seconds in CIM
    vamax: float = 0.0  # Type #PU in CIM
    vamin: float = 0.0  # Type #PU in CIM
    ilr: float = 0.0  # Type #PU in CIM
    klr: float = 0.0  # Type #PU in CIM
    xe: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExcST1A\n"
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
            "vimax": [
                self.profiles.DY.value,
            ],
            "vimin": [
                self.profiles.DY.value,
            ],
            "tc": [
                self.profiles.DY.value,
            ],
            "tb": [
                self.profiles.DY.value,
            ],
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
            "kc": [
                self.profiles.DY.value,
            ],
            "kf": [
                self.profiles.DY.value,
            ],
            "tf": [
                self.profiles.DY.value,
            ],
            "tc1": [
                self.profiles.DY.value,
            ],
            "tb1": [
                self.profiles.DY.value,
            ],
            "vamax": [
                self.profiles.DY.value,
            ],
            "vamin": [
                self.profiles.DY.value,
            ],
            "ilr": [
                self.profiles.DY.value,
            ],
            "klr": [
                self.profiles.DY.value,
            ],
            "xe": [
                self.profiles.DY.value,
            ],
        }
