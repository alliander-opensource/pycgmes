"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcIEEEDC2A(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type DC2A model. This model represents field-controlled DC commutator exciters with continuously
      acting voltage regulators having supplies obtained from the generator or auxiliary bus.  It differs from the
      type DC1A model only in the voltage regulator output limits, which are now proportional to terminal voltage
      VT. It is representative of solid-state replacements for various forms of older mechanical and rotating
      amplifier regulating equipment connected to DC commutator exciters. Reference: IEEE 421.5-2005, 5.2.

    efd1: Exciter voltage at which exciter saturation is defined (EFD1) (> 0).  Typical value = 3,05.
    efd2: Exciter voltage at which exciter saturation is defined (EFD2) (> 0).  Typical value = 2,29.
    exclim: (exclim).  IEEE standard is ambiguous about lower limit on exciter output. Typical value = - 999  which
      means that there is no limit applied.
    ka: Voltage regulator gain (KA) (> 0).  Typical value = 300.
    ke: Exciter constant related to self-excited field (KE).  Typical value = 1.
    kf: Excitation control system stabilizer gain (KF) (>= 0).  Typical value = 0,1.
    seefd1: Exciter saturation function value at the corresponding exciter voltage, EFD1 (SE[EFD1]) (>= 0).  Typical
      value = 0,279.
    seefd2: Exciter saturation function value at the corresponding exciter voltage, EFD2 (SE[EFD2]) (>= 0).  Typical
      value = 0,117.
    ta: Voltage regulator time constant (TA) (> 0).  Typical value = 0,01.
    tb: Voltage regulator time constant (TB) (>= 0).  Typical value = 0.
    tc: Voltage regulator time constant (TC) (>= 0).  Typical value = 0.
    te: Exciter time constant, integration rate associated with exciter control (TE) (> 0).  Typical value = 1,33.
    tf: Excitation control system stabilizer time constant (TF) (> 0).  Typical value = 0,675.
    uelin: UEL input (uelin). true = input is connected to the HV gate false = input connects to the error signal.
      Typical value = true.
    vrmax: Maximum voltage regulator output (VRMAX)(> ExcIEEEDC2A.vrmin).  Typical value = 4,95.
    vrmin: Minimum voltage regulator output (VRMIN) (< 0 and < ExcIEEEDC2A.vrmax).  Typical value = -4,9.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    efd1: float = 0.0  # Type #PU in CIM
    efd2: float = 0.0  # Type #PU in CIM
    exclim: float = 0.0  # Type #PU in CIM
    ka: float = 0.0  # Type #PU in CIM
    ke: float = 0.0  # Type #PU in CIM
    kf: float = 0.0  # Type #PU in CIM
    seefd1: float = 0.0  # Type #Float in CIM
    seefd2: float = 0.0  # Type #Float in CIM
    ta: int = 0  # Type #Seconds in CIM
    tb: int = 0  # Type #Seconds in CIM
    tc: int = 0  # Type #Seconds in CIM
    te: int = 0  # Type #Seconds in CIM
    tf: int = 0  # Type #Seconds in CIM
    uelin: bool = False  # Type #Boolean in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExcIEEEDC2A\n"
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
            "efd1": [
                self.profiles.DY.value,
            ],
            "efd2": [
                self.profiles.DY.value,
            ],
            "exclim": [
                self.profiles.DY.value,
            ],
            "ka": [
                self.profiles.DY.value,
            ],
            "ke": [
                self.profiles.DY.value,
            ],
            "kf": [
                self.profiles.DY.value,
            ],
            "seefd1": [
                self.profiles.DY.value,
            ],
            "seefd2": [
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
            "te": [
                self.profiles.DY.value,
            ],
            "tf": [
                self.profiles.DY.value,
            ],
            "uelin": [
                self.profiles.DY.value,
            ],
            "vrmax": [
                self.profiles.DY.value,
            ],
            "vrmin": [
                self.profiles.DY.value,
            ],
        }
