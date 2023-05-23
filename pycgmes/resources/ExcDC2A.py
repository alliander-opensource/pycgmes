"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcDC2A(ExcitationSystemDynamics):
    """
    Modified IEEE DC2A direct current commutator exciter with speed input, one more leg block in feedback loop and
      without underexcitation limiters (UEL) inputs.  DC type 2 excitation system model with added speed multiplier,
      added lead-lag, and voltage-dependent limits.

    ka: Voltage regulator gain (Ka) (> 0).  Typical value = 300.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical value = 0.
    ta: Voltage regulator time constant (Ta) (> 0).  Typical value = 0,01.
    tb: Voltage regulator time constant (Tb) (>= 0).  Typical value = 0.
    tc: Voltage regulator time constant (Tc) (>= 0).  Typical value = 0.
    vrmax: Maximum voltage regulator output (Vrmax) (> ExcDC2A.vrmin).  Typical value = 4,95.
    vrmin: Minimum voltage regulator output (Vrmin) (< 0 and < ExcDC2A.vrmax).  Typical value = -4,9.
    ke: Exciter constant related to self-excited field (Ke).  If Ke is entered as zero, the model calculates an
      effective value of Ke such that the initial condition value of Vr is zero. The zero value of Ke is not
      changed.  If Ke is entered as non-zero, its value is used directly, without change.  Typical value = 1.
    te: Exciter time constant, integration rate associated with exciter control (Te) (> 0).  Typical value = 1,33.
    kf: Excitation control system stabilizer gain (Kf) (>= 0).  Typical value = 0,1.
    tf: Excitation control system stabilizer time constant (Tf) (> 0).  Typical value = 0,675.
    tf1: Excitation control system stabilizer time constant (Tf1) (>= 0).  Typical value = 0.
    efd1: Exciter voltage at which exciter saturation is defined (Efd1) (> 0).  Typical value = 3,05.
    seefd1: Exciter saturation function value at the corresponding exciter voltage, Efd1 (Se[Efd1]) (>= 0).  Typical
      value = 0,279.
    efd2: Exciter voltage at which exciter saturation is defined (Efd2) (> 0).  Typical value = 2,29.
    seefd2: Exciter saturation function value at the corresponding exciter voltage, Efd2 (Se[Efd2]) (>= 0).  Typical
      value = 0,117.
    exclim: (exclim).  IEEE standard is ambiguous about lower limit on exciter output. true = a lower limit of zero is
      applied to integrator output false = a lower limit of zero is not applied to integrator output.
      Typical value = true.
    vtlim: (Vtlim). true = limiter at the block (Ka / [1 + sTa]) is dependent on Vt  false = limiter at the block is not
      dependent on Vt. Typical value = true.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    ka: float = 0.0  # Type #PU in CIM
    ks: float = 0.0  # Type #PU in CIM
    ta: int = 0  # Type #Seconds in CIM
    tb: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    ke: float = 0.0  # Type #PU in CIM
    te: int = 0  # Type #Seconds in CIM
    kf: float = 0.0  # Type #PU in CIM
    tf: int = 0  # Type #Seconds in CIM
    tf1: int = 0  # Type #Seconds in CIM
    efd1: float = 0.0  # Type #PU in CIM
    seefd1: float = 0.0  # Type #Float in CIM
    efd2: float = 0.0  # Type #PU in CIM
    seefd2: float = 0.0  # Type #Float in CIM
    exclim: bool = False  # Type #Boolean in CIM
    vtlim: bool = False  # Type #Boolean in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExcDC2A\n"
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
            "ta": [
                self.profiles.DY.value,
            ],
            "tb": [
                self.profiles.DY.value,
            ],
            "tc": [
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
            "tf1": [
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
            "exclim": [
                self.profiles.DY.value,
            ],
            "vtlim": [
                self.profiles.DY.value,
            ],
        }
