"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass
class ExcIEEEST5B(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type ST5B model. The type ST5B excitation system is a variation of the type ST1A model, with
      alternative overexcitation and underexcitation inputs and additional limits. The block diagram in the IEEE
      421.5 standard has input signal Vc and does not indicate the summation point with Vref. The implementation of
      the ExcIEEEST5B shall consider summation point with Vref. Reference: IEEE 421.5-2005, 7.5.

    kr: Regulator gain (KR) (> 0).  Typical value = 200.
    t1: Firing circuit time constant (T1) (>= 0).  Typical value = 0,004.
    kc: Rectifier regulation factor (KC) (>= 0).  Typical value = 0,004.
    vrmax: Maximum voltage regulator output (VRMAX) (> 0).  Typical value = 5.
    vrmin: Minimum voltage regulator output (VRMIN) (< 0).  Typical value = -4.
    tc1: Regulator lead time constant (TC1) (>= 0).  Typical value = 0,8.
    tb1: Regulator lag time constant (TB1) (>= 0).  Typical value = 6.
    tc2: Regulator lead time constant (TC2) (>= 0).  Typical value = 0,08.
    tb2: Regulator lag time constant (TB2) (>= 0).  Typical value = 0,01.
    toc1: OEL lead time constant (TOC1) (>= 0).  Typical value = 0,1.
    tob1: OEL lag time constant (TOB1) (>= 0).  Typical value = 2.
    toc2: OEL lead time constant (TOC2) (>= 0).  Typical value = 0,08.
    tob2: OEL lag time constant (TOB2) (>= 0).  Typical value = 0,08.
    tuc1: UEL lead time constant (TUC1) (>= 0).  Typical value = 2.
    tub1: UEL lag time constant (TUB1) (>= 0).  Typical value = 10.
    tuc2: UEL lead time constant (TUC2) (>= 0).  Typical value = 0,1.
    tub2: UEL lag time constant (TUB2) (>= 0).  Typical value = 0,05.
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    kr: float = 0.0  # Type #PU in CIM
    t1: int = 0  # Type #Seconds in CIM
    kc: float = 0.0  # Type #PU in CIM
    vrmax: float = 0.0  # Type #PU in CIM
    vrmin: float = 0.0  # Type #PU in CIM
    tc1: int = 0  # Type #Seconds in CIM
    tb1: int = 0  # Type #Seconds in CIM
    tc2: int = 0  # Type #Seconds in CIM
    tb2: int = 0  # Type #Seconds in CIM
    toc1: int = 0  # Type #Seconds in CIM
    tob1: int = 0  # Type #Seconds in CIM
    toc2: int = 0  # Type #Seconds in CIM
    tob2: int = 0  # Type #Seconds in CIM
    tuc1: int = 0  # Type #Seconds in CIM
    tub1: int = 0  # Type #Seconds in CIM
    tuc2: int = 0  # Type #Seconds in CIM
    tub2: int = 0  # Type #Seconds in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=ExcIEEEST5B\n"
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
            "kr": [
                self.profiles.DY.value,
            ],
            "t1": [
                self.profiles.DY.value,
            ],
            "kc": [
                self.profiles.DY.value,
            ],
            "vrmax": [
                self.profiles.DY.value,
            ],
            "vrmin": [
                self.profiles.DY.value,
            ],
            "tc1": [
                self.profiles.DY.value,
            ],
            "tb1": [
                self.profiles.DY.value,
            ],
            "tc2": [
                self.profiles.DY.value,
            ],
            "tb2": [
                self.profiles.DY.value,
            ],
            "toc1": [
                self.profiles.DY.value,
            ],
            "tob1": [
                self.profiles.DY.value,
            ],
            "toc2": [
                self.profiles.DY.value,
            ],
            "tob2": [
                self.profiles.DY.value,
            ],
            "tuc1": [
                self.profiles.DY.value,
            ],
            "tub1": [
                self.profiles.DY.value,
            ],
            "tuc2": [
                self.profiles.DY.value,
            ],
            "tub2": [
                self.profiles.DY.value,
            ],
        }
