"""
Generated from the CGMES 3 files via cimgen: https://github.com/Alliander/uno-cimgen/
"""

from dataclasses import fields
from functools import cached_property
from pydantic.dataclasses import dataclass
from .Base import DataclassConfig, Profile
from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass(config=DataclassConfig)
class PssPTIST3(PowerSystemStabilizerDynamics):
    """
    PTI microprocessor-based stabilizer type 3.

    m: (M).  M = 2 x H.  Typical value = 5.
    tf: Time constant (Tf) (>= 0).  Typical value = 0,2.
    tp: Time constant (Tp) (>= 0).  Typical value = 0,2.
    t1: Time constant (T1) (>= 0).  Typical value = 0,3.
    t2: Time constant (T2) (>= 0).  Typical value = 1.
    t3: Time constant (T3) (>= 0).  Typical value = 0,2.
    t4: Time constant (T4) (>= 0).  Typical value = 0,05.
    k: Gain (K).  Typical value = 9.
    dtf: Time step frequency calculation (deltatf) (>= 0).  Typical value = 0,025 (0,03 for 50 Hz).
    dtc: Time step related to activation of controls (deltatc) (>= 0).  Typical value = 0,025 (0,03 for 50 Hz).
    dtp: Time step active power calculation (deltatp) (>= 0).  Typical value = 0,0125  (0,015 for 50 Hz).
    t5: Time constant (T5) (>= 0).
    t6: Time constant (T6) (>= 0).
    a0: Filter coefficient (A0).
    a1: Limiter (Al).
    a2: Filter coefficient (A2).
    b0: Filter coefficient (B0).
    b1: Filter coefficient (B1).
    b2: Filter coefficient (B2).
    a3: Filter coefficient (A3).
    a4: Filter coefficient (A4).
    a5: Filter coefficient (A5).
    b3: Filter coefficient (B3).
    b4: Filter coefficient (B4).
    b5: Filter coefficient (B5).
    athres: Threshold value above which output averaging will be bypassed (Athres).  Typical value = 0,005.
    dl: Limiter (Dl).
    al: Limiter (Al).
    lthres: Threshold value (Lthres).
    pmin: (Pmin).
    isw: Digital/analogue output switch (Isw). true = produce analogue output false = convert to digital output, using
      tap selection table.
    nav: Number of control outputs to average (NAV) (1 <=  NAV <= 16).  Typical value = 4.
    ncl: Number of counts at limit to active limit function (NCL) (> 0).
    ncr: Number of counts until reset after limit function is triggered (NCR).
    """

    m: float = 0.0  # Type #PU in CIM
    tf: int = 0  # Type #Seconds in CIM
    tp: int = 0  # Type #Seconds in CIM
    t1: int = 0  # Type #Seconds in CIM
    t2: int = 0  # Type #Seconds in CIM
    t3: int = 0  # Type #Seconds in CIM
    t4: int = 0  # Type #Seconds in CIM
    k: float = 0.0  # Type #PU in CIM
    dtf: int = 0  # Type #Seconds in CIM
    dtc: int = 0  # Type #Seconds in CIM
    dtp: int = 0  # Type #Seconds in CIM
    t5: int = 0  # Type #Seconds in CIM
    t6: int = 0  # Type #Seconds in CIM
    a0: float = 0.0  # Type #PU in CIM
    a1: float = 0.0  # Type #PU in CIM
    a2: float = 0.0  # Type #PU in CIM
    b0: float = 0.0  # Type #PU in CIM
    b1: float = 0.0  # Type #PU in CIM
    b2: float = 0.0  # Type #PU in CIM
    a3: float = 0.0  # Type #PU in CIM
    a4: float = 0.0  # Type #PU in CIM
    a5: float = 0.0  # Type #PU in CIM
    b3: float = 0.0  # Type #PU in CIM
    b4: float = 0.0  # Type #PU in CIM
    b5: float = 0.0  # Type #PU in CIM
    athres: float = 0.0  # Type #PU in CIM
    dl: float = 0.0  # Type #PU in CIM
    al: float = 0.0  # Type #PU in CIM
    lthres: float = 0.0  # Type #PU in CIM
    pmin: float = 0.0  # Type #PU in CIM
    isw: bool = False  # Type #Boolean in CIM
    nav: float = 0.0  # Type #Float in CIM
    ncl: float = 0.0  # Type #Float in CIM
    ncr: float = 0.0  # Type #Float in CIM

    def __str__(self) -> str:
        """Returns the string represention of this element."""

        return "\n".join(
            ["class=PssPTIST3"] + [f"{field.name}={getattr(self, field.name)}" for field in fields(self.__class__)]
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
            "m": [
                Profile.DY.value,
            ],
            "tf": [
                Profile.DY.value,
            ],
            "tp": [
                Profile.DY.value,
            ],
            "t1": [
                Profile.DY.value,
            ],
            "t2": [
                Profile.DY.value,
            ],
            "t3": [
                Profile.DY.value,
            ],
            "t4": [
                Profile.DY.value,
            ],
            "k": [
                Profile.DY.value,
            ],
            "dtf": [
                Profile.DY.value,
            ],
            "dtc": [
                Profile.DY.value,
            ],
            "dtp": [
                Profile.DY.value,
            ],
            "t5": [
                Profile.DY.value,
            ],
            "t6": [
                Profile.DY.value,
            ],
            "a0": [
                Profile.DY.value,
            ],
            "a1": [
                Profile.DY.value,
            ],
            "a2": [
                Profile.DY.value,
            ],
            "b0": [
                Profile.DY.value,
            ],
            "b1": [
                Profile.DY.value,
            ],
            "b2": [
                Profile.DY.value,
            ],
            "a3": [
                Profile.DY.value,
            ],
            "a4": [
                Profile.DY.value,
            ],
            "a5": [
                Profile.DY.value,
            ],
            "b3": [
                Profile.DY.value,
            ],
            "b4": [
                Profile.DY.value,
            ],
            "b5": [
                Profile.DY.value,
            ],
            "athres": [
                Profile.DY.value,
            ],
            "dl": [
                Profile.DY.value,
            ],
            "al": [
                Profile.DY.value,
            ],
            "lthres": [
                Profile.DY.value,
            ],
            "pmin": [
                Profile.DY.value,
            ],
            "isw": [
                Profile.DY.value,
            ],
            "nav": [
                Profile.DY.value,
            ],
            "ncl": [
                Profile.DY.value,
            ],
            "ncr": [
                Profile.DY.value,
            ],
        }
