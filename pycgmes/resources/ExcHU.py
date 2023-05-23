"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcHU(ExcitationSystemDynamics):
    """
    Hungarian excitation system, with built-in voltage transducer.

    tr: Filter time constant (Tr) (>= 0). If a voltage compensator is used in conjunction with this excitation system
      model, Tr should be set to 0.  Typical value = 0,01.
    te: Major loop PI tag integration time constant (Te) (>= 0).  Typical value = 0,154.
    imin: Major loop PI tag output signal lower limit (Imin) (< ExcHU.imax).  Typical value = 0,1.
    imax: Major loop PI tag output signal upper limit (Imax) (> ExcHU.imin).  Typical value = 2,19.
    ae: Major loop PI tag gain factor (Ae).  Typical value = 3.
    emin: Field voltage control signal lower limit on AVR base (Emin) (< ExcHU.emax).  Typical value = -0,866.
    emax: Field voltage control signal upper limit on AVR base (Emax) (> ExcHU.emin).  Typical value = 0,996.
    ki: Current base conversion constant (Ki).  Typical value = 0,21428.
    ai: Minor loop PI tag gain factor (Ai).  Typical value = 22.
    ti: Minor loop PI control tag integration time constant (Ti) (>= 0).  Typical value = 0,01333.
    atr: AVR constant (Atr).  Typical value = 2,19.
    ke: Voltage base conversion constant (Ke).  Typical value = 4,666.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    tr: int = 0  # Type #Seconds in CIM
    te: int = 0  # Type #Seconds in CIM
    imin: float = 0.0  # Type #PU in CIM
    imax: float = 0.0  # Type #PU in CIM
    ae: float = 0.0  # Type #PU in CIM
    emin: float = 0.0  # Type #PU in CIM
    emax: float = 0.0  # Type #PU in CIM
    ki: float = 0.0  # Type #Float in CIM
    ai: float = 0.0  # Type #PU in CIM
    ti: int = 0  # Type #Seconds in CIM
    atr: float = 0.0  # Type #PU in CIM
    ke: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExcHU\n"
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
            "tr": [
                self.profiles.DY.value,
            ],
            "te": [
                self.profiles.DY.value,
            ],
            "imin": [
                self.profiles.DY.value,
            ],
            "imax": [
                self.profiles.DY.value,
            ],
            "ae": [
                self.profiles.DY.value,
            ],
            "emin": [
                self.profiles.DY.value,
            ],
            "emax": [
                self.profiles.DY.value,
            ],
            "ki": [
                self.profiles.DY.value,
            ],
            "ai": [
                self.profiles.DY.value,
            ],
            "ti": [
                self.profiles.DY.value,
            ],
            "atr": [
                self.profiles.DY.value,
            ],
            "ke": [
                self.profiles.DY.value,
            ],
        }
