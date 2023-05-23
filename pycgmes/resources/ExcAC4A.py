"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcAC4A(ExcitationSystemDynamics):
    """
    Modified IEEE AC4A alternator-supplied rectifier excitation system with different minimum controller output.

    vimax: Maximum voltage regulator input limit (Vimax)  (> 0).  Typical value = 10.
    vimin: Minimum voltage regulator input limit (Vimin) (< 0).  Typical value = -10.
    tc: Voltage regulator time constant (Tc) (>= 0).  Typical value = 1.
    tb: Voltage regulator time constant (Tb) (>= 0).  Typical value = 10.
    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 200.
    ta: Voltage regulator time constant (Ta) (> 0).  Typical value = 0,015.
    vrmax: Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 5,64.
    vrmin: Minimum voltage regulator output (Vrmin) (< 0).  Typical value = -4,53.
    kc: Rectifier loading factor proportional to commutating reactance (Kc) (>= 0).  Typical value = 0.
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

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExcAC4A\n"
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
        }
