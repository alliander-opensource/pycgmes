"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcAC5A(ExcitationSystemDynamics):
    """
    Modified IEEE AC5A alternator-supplied rectifier excitation system with different minimum controller output.

    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 400.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical value = 0.
    tb: Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.
    tc: Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.
    ta: Voltage regulator time constant (Ta) (> 0).  Typical value = 0,02.
    vrmax: Maximum voltage regulator output (Vrmax) (> 0).  Typical value = 7,3.
    vrmin: Minimum voltage regulator output (Vrmin) (< 0).  Typical value =-7,3.
    ke: Exciter constant related to self-excited field (Ke).  Typical value = 1.
    te: Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 0,8.
    kf: Excitation control system stabilizer gains (Kf) (>= 0).  Typical value = 0,03.
    tf1: Excitation control system stabilizer time constant (Tf1) (> 0).  Typical value  = 1.
    tf2: Excitation control system stabilizer time constant (Tf2) (>= 0).  Typical value = 0,8.
    tf3: Excitation control system stabilizer time constant (Tf3) (>= 0).  Typical value = 0.
    efd1: Exciter voltage at which exciter saturation is defined (Efd1) (> 0).  Typical value = 5,6.
    seefd1: Exciter saturation function value at the corresponding exciter voltage, Efd1 (Se[Efd1]) (>= 0).  Typical
      value = 0,86.
    efd2: Exciter voltage at which exciter saturation is defined (Efd2) (> 0).  Typical value = 4,2.
    seefd2: Exciter saturation function value at the corresponding exciter voltage, Efd2 (Se[Efd2]) (>= 0).  Typical
      value = 0,5.
    a: Coefficient to allow different usage of the model (a).  Typical value = 1.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ka: float = 0.0  # Type #PU in CIM
    ks: float = 0.0  # Type #PU in CIM
    tb: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM
    ta: int = 0  # Type #Seconds in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    ke: float = 0.0  # Type #PU in CIM
    te: int = 0  # Type #Seconds in CIM
    kf: float = 0.0  # Type #PU in CIM
    tf1: int = 0  # Type #Seconds in CIM
    tf2: int = 0  # Type #Seconds in CIM
    tf3: int = 0  # Type #Seconds in CIM
    efd1: float = 0.0  # Type #PU in CIM
    seefd1: float = 0.0  # Type #Float in CIM
    efd2: float = 0.0  # Type #PU in CIM
    seefd2: float = 0.0  # Type #Float in CIM
    a: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExcAC5A\n"
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
            "ks": [
                self.profiles.DY.value,
            ],
            "tb": [
                self.profiles.DY.value,
            ],
            "tc": [
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
            "tf1": [
                self.profiles.DY.value,
            ],
            "tf2": [
                self.profiles.DY.value,
            ],
            "tf3": [
                self.profiles.DY.value,
            ],
            "efd1": [
                self.profiles.DY.value,
            ],
            "seefd1": [
                self.profiles.DY.value,
            ],
            "efd2": [
                self.profiles.DY.value,
            ],
            "seefd2": [
                self.profiles.DY.value,
            ],
            "a": [
                self.profiles.DY.value,
            ],
        }
