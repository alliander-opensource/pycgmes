"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcRQB(ExcitationSystemDynamics):
    """
    Excitation system type RQB (four-loop regulator, r?gulateur quatre boucles, developed in France) primarily used in
      nuclear or thermal generating units. This excitation system shall be always used together with power system
      stabilizer type PssRQB.

    ki0: Voltage reference input gain (Ki0).  Typical value = 12,7.
    ki1: Voltage input gain (Ki1).  Typical value = -16,8.
    te: Lead lag time constant (TE) (>= 0).  Typical value = 0,22.
    tc: Lead lag time constant (TC) (>= 0).  Typical value = 0,02.
    klir: OEL input gain (KLIR).  Typical value = 12,13.
    ucmin: Minimum voltage reference limit (UCMIN) (< ExcRQB.ucmax).  Typical value = 0,9.
    ucmax: Maximum voltage reference limit (UCMAX) (> ExcRQB.ucmin).  Typical value = 1,1.
    lus: Setpoint (LUS).  Typical value = 0,12.
    klus: Limiter gain (KLUS).  Typical value = 50.
    mesu: Voltage input time constant (MESU) (>= 0).  Typical value = 0,02.
    t4m: Input time constant (T4M) (>= 0).  Typical value = 5.
    lsat: Integrator limiter (LSAT).  Typical value = 5,73.
    tf: Exciter time constant (TF) (>= 0).  Typical value = 0,01.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ki0: float = 0.0  # Type #Float in CIM
    ki1: float = 0.0  # Type #Float in CIM
    te: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM
    klir: float = 0.0  # Type #Float in CIM
    ucmin: float = 0.0  # Type #PU in CIM
    ucmax: float = 0.0  # Type #PU in CIM
    lus: float = 0.0  # Type #PU in CIM
    klus: float = 0.0  # Type #Float in CIM
    mesu: int = 0  # Type #Seconds in CIM
    t4m: int = 0  # Type #Seconds in CIM
    lsat: float = 0.0  # Type #PU in CIM
    tf: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExcRQB\n"
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
            "ki0": [
                self.profiles.DY.value,
            ],
            "ki1": [
                self.profiles.DY.value,
            ],
            "te": [
                self.profiles.DY.value,
            ],
            "tc": [
                self.profiles.DY.value,
            ],
            "klir": [
                self.profiles.DY.value,
            ],
            "ucmin": [
                self.profiles.DY.value,
            ],
            "ucmax": [
                self.profiles.DY.value,
            ],
            "lus": [
                self.profiles.DY.value,
            ],
            "klus": [
                self.profiles.DY.value,
            ],
            "mesu": [
                self.profiles.DY.value,
            ],
            "t4m": [
                self.profiles.DY.value,
            ],
            "lsat": [
                self.profiles.DY.value,
            ],
            "tf": [
                self.profiles.DY.value,
            ],
        }
