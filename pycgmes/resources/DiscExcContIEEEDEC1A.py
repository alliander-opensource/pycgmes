"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""
from dataclasses import dataclass, field
from functools import cached_property

from .DiscontinuousExcitationControlDynamics import (
    DiscontinuousExcitationControlDynamics,
)


@dataclass
class DiscExcContIEEEDEC1A(DiscontinuousExcitationControlDynamics):
    """
    IEEE type DEC1A discontinuous excitation control model that boosts generator excitation to a level higher than that
      demanded by the voltage regulator and stabilizer immediately following a system fault. Reference: IEEE
      421.5-2005, 12.2.

    vtlmt: Voltage reference (VTLMT).  Typical value = 1,1.
    vomax: Limiter (VOMAX) (> DiscExcContIEEEDEC1A.vomin).  Typical value = 0,3.
    vomin: Limiter (VOMIN) (< DiscExcContIEEEDEC1A.vomax).  Typical value = 0,1.
    ketl: Terminal voltage limiter gain (KETL).  Typical value = 47.
    vtc: Terminal voltage level reference (VTC).  Typical value = 0,95.
    val: Regulator voltage reference (VAL).  Typical value = 5,5.
    esc: Speed change reference (ESC).  Typical value = 0,0015.
    kan: Discontinuous controller gain (KAN).  Typical value = 400.
    tan: Discontinuous controller time constant (TAN) (>= 0).  Typical value = 0,08.
    tw5: DEC washout time constant (TW5) (>= 0).  Typical value = 5.
    vsmax: Limiter (VSMAX)(> DiscExcContIEEEDEC1A.vsmin).  Typical value = 0,2.
    vsmin: Limiter (VSMIN) (< DiscExcContIEEEDEC1A.vsmax).  Typical value = -0,066.
    td: Time constant (TD) (>= 0).  Typical value = 0,03.
    tl1: Time constant (TL1) (>= 0).  Typical value = 0,025.
    tl2: Time constant (TL2) (>= 0).  Typical value = 1,25.
    vtm: Voltage limits (VTM).  Typical value = 1,13.
    vtn: Voltage limits (VTN).  Typical value = 1,12.
    vanmax: Limiter for Van (VANMAX).
    """

    # Not real data, but used by export
    serializationProfile: dict = field(default_factory=dict, init=False)

    vtlmt: float = 0.0  # Type #PU in CIM
    vomax: float = 0.0  # Type #PU in CIM
    vomin: float = 0.0  # Type #PU in CIM
    ketl: float = 0.0  # Type #PU in CIM
    vtc: float = 0.0  # Type #PU in CIM
    val: float = 0.0  # Type #PU in CIM
    esc: float = 0.0  # Type #PU in CIM
    kan: float = 0.0  # Type #PU in CIM
    tan: int = 0  # Type #Seconds in CIM
    tw5: int = 0  # Type #Seconds in CIM
    vsmax: float = 0.0  # Type #PU in CIM
    vsmin: float = 0.0  # Type #PU in CIM
    td: int = 0  # Type #Seconds in CIM
    tl1: int = 0  # Type #Seconds in CIM
    tl2: int = 0  # Type #Seconds in CIM
    vtm: float = 0.0  # Type #PU in CIM
    vtn: float = 0.0  # Type #PU in CIM
    vanmax: float = 0.0  # Type #PU in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""
        str_ = "class=DiscExcContIEEEDEC1A\n"
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
            "vtlmt": [
                self.profiles.DY.value,
            ],
            "vomax": [
                self.profiles.DY.value,
            ],
            "vomin": [
                self.profiles.DY.value,
            ],
            "ketl": [
                self.profiles.DY.value,
            ],
            "vtc": [
                self.profiles.DY.value,
            ],
            "val": [
                self.profiles.DY.value,
            ],
            "esc": [
                self.profiles.DY.value,
            ],
            "kan": [
                self.profiles.DY.value,
            ],
            "tan": [
                self.profiles.DY.value,
            ],
            "tw5": [
                self.profiles.DY.value,
            ],
            "vsmax": [
                self.profiles.DY.value,
            ],
            "vsmin": [
                self.profiles.DY.value,
            ],
            "td": [
                self.profiles.DY.value,
            ],
            "tl1": [
                self.profiles.DY.value,
            ],
            "tl2": [
                self.profiles.DY.value,
            ],
            "vtm": [
                self.profiles.DY.value,
            ],
            "vtn": [
                self.profiles.DY.value,
            ],
            "vanmax": [
                self.profiles.DY.value,
            ],
        }
