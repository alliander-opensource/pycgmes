"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics


@dataclass(config=DataclassConfig)
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

        return "\n".join(
            ["class=DiscExcContIEEEDEC1A"]
            + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
        )

    @cached_property
    def possible_profiles(self) -> dict[str, list]:
        """
        A resource can be used by multiple profiles. This is the list of profiles
        where this element or its attributes can be found.
        """
        return {
            # Class itself
            "class": [
                Profile.DY.value,
            ],
            # Attributes
            "vtlmt": [
                Profile.DY.value,
            ],
            "vomax": [
                Profile.DY.value,
            ],
            "vomin": [
                Profile.DY.value,
            ],
            "ketl": [
                Profile.DY.value,
            ],
            "vtc": [
                Profile.DY.value,
            ],
            "val": [
                Profile.DY.value,
            ],
            "esc": [
                Profile.DY.value,
            ],
            "kan": [
                Profile.DY.value,
            ],
            "tan": [
                Profile.DY.value,
            ],
            "tw5": [
                Profile.DY.value,
            ],
            "vsmax": [
                Profile.DY.value,
            ],
            "vsmin": [
                Profile.DY.value,
            ],
            "td": [
                Profile.DY.value,
            ],
            "tl1": [
                Profile.DY.value,
            ],
            "tl2": [
                Profile.DY.value,
            ],
            "vtm": [
                Profile.DY.value,
            ],
            "vtn": [
                Profile.DY.value,
            ],
            "vanmax": [
                Profile.DY.value,
            ],
        }
