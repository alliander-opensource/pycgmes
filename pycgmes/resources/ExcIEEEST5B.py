"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .ExcitationSystemDynamics import ExcitationSystemDynamics


@dataclass(config=DataclassConfig)
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

        return "\n".join(
            ["class=ExcIEEEST5B"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "kr": [
                Profile.DY.value,
            ],
            "t1": [
                Profile.DY.value,
            ],
            "kc": [
                Profile.DY.value,
            ],
            "vrmax": [
                Profile.DY.value,
            ],
            "vrmin": [
                Profile.DY.value,
            ],
            "tc1": [
                Profile.DY.value,
            ],
            "tb1": [
                Profile.DY.value,
            ],
            "tc2": [
                Profile.DY.value,
            ],
            "tb2": [
                Profile.DY.value,
            ],
            "toc1": [
                Profile.DY.value,
            ],
            "tob1": [
                Profile.DY.value,
            ],
            "toc2": [
                Profile.DY.value,
            ],
            "tob2": [
                Profile.DY.value,
            ],
            "tuc1": [
                Profile.DY.value,
            ],
            "tub1": [
                Profile.DY.value,
            ],
            "tuc2": [
                Profile.DY.value,
            ],
            "tub2": [
                Profile.DY.value,
            ],
        }
